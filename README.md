# Generative Deep Learning Framework with Guided Embedding Modifier (GEM): Improving Package Design Using Eye Movements

> Package design plays a critical role at the point of purchase. Prior literature does not provide a comprehensive methodology that enables managers to design packages that are easy to find, while communicating their brand identity. This research addresses this gap by introducing a novel framework that integrates generative deep learning architectures with eye-movement data, which aims to make the following three contributions. First, it extends the standard generative deep learning framework by incorporating a Guided Embedding Modifier (GEM). This novel module allows the latent embedding space of existing package designs to be transformed in a guided manner, such that the transformation results in an improved package that is easier to find. Second, building on a two-stage eye-movement model of visual search, it successfully links package design embeddings to the eye movements of consumers. This model serves as input for the GEM component and generates counterfactual scanpaths to predict the performance of a newly generated package design. Third, to validate the performance of the approach, a follow-up online experiment confirms that consumers are able to find the newly designed packages faster than their original versions, demonstrating the practical relevance.



## Description   
> Implementation of GEM framework for package design. Inspired on the pSp method and StyleGAN, we extend the framework with a Guided Embedding Modifier (GEM) that integrates eye‑movement data into the image-to-image translation process，enabling the redesign of packages that are easier for consumers to find.

## Table of Contents
  * [Description](#description)
  * [Table of Contents](#table-of-contents)
  * [Getting Started](#getting-started)
    + [Prerequisites](#prerequisites)
    + [Installation](#installation)
    + [Pretrained Models](#pretrained-models)
  * [Package Encoder and Generator](#package-encoder-andgenerator)
    + [Preparing Data](#preparing-data)
    + [Training Generator](#training-generator)
    + [Training Encoder](#training-encoder)
  * [Eye Movement Model](#eye-movement-model)
    + [Eye Movement Data](#eye-movement-data)
    + [Run Eye Movement Model](#run-eye-movement-model)


## Getting Started
### Prerequisites
- Linux or macOS
- NVIDIA GPU + CUDA CuDNN (CPU may be possible with some modifications, but is not inherently supported)
- Python 2 or 3

### Installation
- Clone this repo:
``` 
git clone https://github.com/PackageGEM/GEM.git
cd GEM
```
- Dependencies:  
We recommend running this repository using [Anaconda](https://docs.anaconda.com/anaconda/install/). 
All dependencies for defining the environment are provided in `environment/GEM.yaml`.
 

### Pretrained Models
Please download the pre-trained models from the following links.
|[Encoder and Generator pre-trained models](https://drive.google.com/drive/folders/1lmRSSdJes-N-fGo5ZdKG35TP8HUA7pBs?usp=drive_link) 

## Package Encoder and Generator
### Preparing Data
- Please see the shampoo dateset in the following link: https://drive.google.com/drive/folders/1ndpOzA9H-giD6Q6dzARJJgqj2AmegCMr?usp=drive_link


### Training Generator
Create LMDB datasets
```
python prepare_data.py \
--out LMDB_PATH \
--n_worker N_WORKER \
--size SIZE1,SIZE2,SIZE3,... \
DATASET_PATH
```

Train the generator (supports distributed training)
```
python -m torch.distributed.launch \
--nproc_per_node=N_GPU \
--master_port=PORT \
./Encoder\ and\ Generator/Generator/train.py \
--batch BATCH_SIZE \
LMDB_PATH
```


### Training Decoder
```
python ./Encoder and Generator/Encoder/scripts/train.py \
--dataset_type=ffhq_encode \
--exp_dir=/path/to/experiment \
--checkpoint_path=/path/to/checkpoint\
--workers=8 \
--batch_size=2 \
--test_batch_size=2 \
--test_workers=8 \
--val_interval=2500 \
--save_interval=10000 \
--encoder_type=GradualStyleEncoder \
--start_from_latent_avg \
--lpips_lambda=0.8 \
--l2_lambda=1.5 \
--id_lambda=0.1 \
--output_size=256 \
```

## Eye Movement Model
### Eye Movement Data
Eyetracking data are avaliable in the ./Data/Eyetracking/.... For details on the data cleaning procedure, please refer to the main paper in the Data Processing section under Eye‑Tracking Study of Visual Search. The folllowing scripts map each fixation to the corresponding product and extract the corresponding behaviors in the search sequence.
To preprocess the data, run:
> python ./Data/Eyetracking/preprocessing/label.py
> python ./Data/Eyetracking/preprocessing/behavior.py

During preprocessing, we derive the following variables:
- Similarity variable — computed as the cosine similarity between the embedding of the target package and the embeddings of each shelf package. The embeddings are generated using the trained encoder.
- Saliency variable — computed with the Itti–Koch–Niebur (2002) model; saliency maps are created from low‑level visual features, and values are averaged within each package region.
- Package design variable — obtained from the package encoder. We apply rotated PCA with a custom criterion: each component in the embedding must explain at least 1% of the variance.

### Run Run Eye Movement Model
> python ./Eye-Movement Model/Three-Layer Hierarchical Multinomial Probit.py

 