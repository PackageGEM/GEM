import numpy as np
from numpy.linalg import inv, cholesky
from scipy.stats import multivariate_normal, bernoulli, invwishart, truncnorm

# ==============================================================
# Utility Functions
# ==============================================================

def sample_truncated_normal(mean, sd, lower, upper, size=1):
    a, b = (lower - mean) / sd, (upper - mean) / sd
    return truncnorm.rvs(a, b, loc=mean, scale=sd, size=size)

def sample_mvn(mean, cov):
    return multivariate_normal.rvs(mean=mean, cov=cov)

# ==============================================================
# Hierarchical Multinomial Probit with SSVS
# ==============================================================

class HierarchicalProbitSSVS:
    def __init__(self, X, Z, V, Y, N=2000, Nb=1000, tau=2, pi=0.5):
        """
        X: observation-level covariates [I,K,J,T,d]
        Z: task-level covariates [I,K,d,p]
        V: individual-level covariates [I,q]
        Y: observed choices [I,K,J,T]
        N: number of posterior samples
        Nb: burn-in iterations
        tau: thinning
        pi: prior inclusion probability (SSVS)
        """
        self.X, self.Z, self.V, self.Y = X, Z, V, Y
        self.I, self.K, self.J, self.T, self.d = X.shape
        _, _, _, self.p = Z.shape
        self.q = V.shape[1]
        
        self.N, self.Nb, self.tau, self.pi = N, Nb, tau, pi
        
        # Hyperparameters
        self.u0 = np.zeros(self.q)              
        self.V0 = np.eye(self.q)                
        self.f0 = self.d + 2                   
        self.G0 = np.eye(self.q)               
        self.r0 = self.p + 2                    
        self.S0 = np.eye(self.d)                
        
        # Initialize parameters
        self.Theta = np.zeros((self.q,))
        self.Lambda = np.eye(self.q)
        self.Psi = np.eye(self.d)
        self.A = np.random.normal(size=(self.I, self.q))
        self.B = np.random.normal(size=(self.I, self.K, self.d))
        self.Gamma = np.random.binomial(1, pi, size=(self.I, self.K, self.d, self.p))
        
        # Containers for posterior samples
        self.samples = {
            "Theta": [], "Lambda": [], "Psi": [],
            "A": [], "B": [], "Gamma": []
        }

    # --------------------------------------------------------------
    # Step 1: Update B_ik (task-specific coefficients)
    # --------------------------------------------------------------
    def update_B(self):
        for i in range(self.I):
            for k in range(self.K):
                X_ik = self.X[i, k].reshape(-1, self.d)
                U_ik = self.U[i, k].reshape(-1, 1)
                Z_gamma = (self.Z[i,k] * self.Gamma[i,k]) @ self.A[i]
                
                Q = inv((X_ik.T @ X_ik) + inv(self.Psi))
                q = Q @ (X_ik.T @ U_ik + inv(self.Psi) @ Z_gamma)
                self.B[i,k] = sample_mvn(q.ravel(), Q)

    # --------------------------------------------------------------
    # Step 2: Update A_i (individual-specific coefficients)
    # --------------------------------------------------------------
    def update_A(self):
        for i in range(self.I):
            Z_gamma = []
            B_vec = []
            for k in range(self.K):
                Z_gamma.append(self.Z[i,k] * self.Gamma[i,k])
                B_vec.append(self.B[i,k])
            Z_gamma = np.vstack(Z_gamma)
            B_vec = np.hstack(B_vec)
            
            Q = inv(Z_gamma.T @ inv(self.Psi) @ Z_gamma + inv(self.Lambda))
            q = Q @ (Z_gamma.T @ inv(self.Psi) @ B_vec + inv(self.Lambda) @ self.Theta)
            self.A[i] = sample_mvn(q, Q)

    # --------------------------------------------------------------
    # Step 3: Update Θ (population-level coefficients)
    # --------------------------------------------------------------
    def update_Theta(self):
        A_star = self.A.reshape(-1, self.q)
        Q = inv(self.V.T @ self.V + inv(self.V0))
        q = Q @ (self.V.T @ A_star.mean(axis=0) + inv(self.V0) @ self.u0)
        self.Theta = sample_mvn(q, Q)

    # --------------------------------------------------------------
    # Step 4: Update covariance matrices Λ and Ψ
    # --------------------------------------------------------------
    def update_covariances(self):
        # Update Lambda
        f_n = self.f0 + self.I
        Gn = self.G0 + ((self.A - self.V @ self.Theta).T @ (self.A - self.V @ self.Theta))
        self.Lambda = invwishart.rvs(df=f_n, scale=Gn)

        # Update Psi
        residuals = []
        for i in range(self.I):
            for k in range(self.K):
                mean = (self.Z[i,k] * self.Gamma[i,k]) @ self.A[i]
                residuals.append(np.outer(self.B[i,k] - mean, self.B[i,k] - mean))
        Sk = sum(residuals) + self.S0
        self.Psi = invwishart.rvs(df=self.r0 + self.I*self.K, scale=Sk)

    # --------------------------------------------------------------
    # Step 5: Update inclusion indicators Γ (SSVS)
    # --------------------------------------------------------------
    def update_Gamma(self):
        for i in range(self.I):
            for k in range(self.K):
                for d in range(self.d):
                    for r in range(self.p):
                        g1 = self.Gamma[i,k].copy()
                        g1[d,r] = 1
                        g0 = self.Gamma[i,k].copy()
                        g0[d,r] = 0
                        
                        mean1 = (self.Z[i,k] * g1) @ self.A[i]
                        mean0 = (self.Z[i,k] * g0) @ self.A[i]
                        
                        ll1 = multivariate_normal.pdf(self.B[i,k], mean=mean1, cov=self.Psi)
                        ll0 = multivariate_normal.pdf(self.B[i,k], mean=mean0, cov=self.Psi)
                        
                        prob = self.pi*ll1 / (self.pi*ll1 + (1-self.pi)*ll0 + 1e-12)
                        self.Gamma[i,k,d,r] = bernoulli.rvs(prob)

    # --------------------------------------------------------------
    # Step 6: Update latent utilities U
    # --------------------------------------------------------------
    def update_U(self):
        self.U = np.zeros((self.I, self.K, self.J, self.T))
        for i in range(self.I):
            for k in range(self.K):
                for t in range(self.T):
                    mu = self.X[i,k,:,t,:] @ self.B[i,k]
                    chosen = np.argmax(self.Y[i,k,:,t])
                    for j in range(self.J):
                        if self.Y[i,k,j,t] == 1:
                            self.U[i,k,j,t] = sample_truncated_normal(mu[j], 1, 0, np.inf)
                        else:
                            max_other = max(mu[l] for l in range(self.J) if l != j)
                            self.U[i,k,j,t] = sample_truncated_normal(mu[j], 1, -np.inf, max_other)

    # --------------------------------------------------------------
    # Main Sampler
    # --------------------------------------------------------------
    def run(self):
        for n in range(1, self.N+1):
            self.update_U()
            self.update_B()
            self.update_A()
            self.update_Theta()
            self.update_covariances()
            self.update_Gamma()

            if n > self.Nb and (n - self.Nb) % self.tau == 0:
                self.samples["Theta"].append(self.Theta.copy())
                self.samples["Lambda"].append(self.Lambda.copy())
                self.samples["Psi"].append(self.Psi.copy())
                self.samples["A"].append(self.A.copy())
                self.samples["B"].append(self.B.copy())
                self.samples["Gamma"].append(self.Gamma.copy())

        # Compute Posterior Inclusion Probabilities (PIP)
        gamma_samples = np.array(self.samples["Gamma"])
        self.PIP = gamma_samples.mean(axis=0)
        return self.samples, self.PIP