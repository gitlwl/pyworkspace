'''
np.random.RandomState.rand()
返回一个[0,1)之间的随机数
np.random.RandomState.rand(维度) 维度为空，返回标量
'''
import numpy as np

rdm=np.random.RandomState(seed=1)#seed=常数每次生成随机数相同
a=rdm.rand() #返回一个随机标量
b=rdm.rand(2,3) #返回维度为2行3列随机数矩阵
print("a:",a)
print("b:",b)


