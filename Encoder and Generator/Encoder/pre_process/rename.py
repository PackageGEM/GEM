
import os

DATADIR = "./data/"
data_k = 'shampoo/'
path = os.path.join(DATADIR, data_k)
#返回path路径下所有文件的名字，以及文件夹的名字，
img_list = os.listdir(path)      

n=0
for i in img_list:

    #设置旧文件名（就是路径+文件名）
    oldname=path+img_list[n]

    #设置新文件名
    newname=path+'shampoo'+str(n+1988)+'.jpg'

    #用os模块中的rename方法对文件改名
    os.rename(oldname,newname)
    print(oldname,'======>',newname)

    n+=1
    