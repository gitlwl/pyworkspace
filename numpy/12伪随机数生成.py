import  numpy as np

'''
rand

产生指定形状的均匀分布的样本值

randint

从给定的上下限范围内选取随机整数

randn

产生正态分布（平均值为0，标准差为1）的样本值，类似于MATLAB接口

binomial

产生二项分布的样本值

normal

产生正态（高斯）分布的样本值

beta

产生Beta分布的样本值

chisquare

产生卡方分布的样本值

gamma

产生Gamma分布的样本值

uniform

产生在指定范围中均匀分布的样本值

seed

确定随机数生成器的种子

permutation

返回一个序列的随机排列或返回一个随机排列的范围

shuffle

对一个序列就地随机排列
'''
print(np.random.randn(3,4))

print(np.random.randint(5,size=(3,4)))
print(np.random.randn(2,4))

mu,sigma=0,0.1
print(np.random.normal(mu,sigma,10))
#参数：low ,high ,size
print(np.random.uniform(1,2,100))