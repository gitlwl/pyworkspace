import numpy as np

'''
索引和切片
数组切片是原始数组的视图，不是复制品，如果要得到切片的副本，应该使用copy()方法
在多维数组中索引，如果省略了后面的索引，则返回对象会是一个维度低一点的ndarray（它含有高一级维度上的所有数据）
1、切片
切片的基本语法 ndarray[i : j : k]，其中i为起始下标，j为结束下标（不包括j），k为步长（默认为1）
'''

arr = np.arange(10)
print(arr)
print(arr[1:9:2])
print(arr[4:-3])

print(arr[9:4:-2])
a=arr[::2]
print(a)
arr[:6]=0
print(arr[6:])
arr[:]=1
print(arr)
print('---------------------------')
#多维切片
ndarr=np.arange(16).reshape((4,4))
print(ndarr)
print(ndarr[:2])# 行，等效于arr2[:2, :]
# 前两行的前两列
print(ndarr[:2,:2])
# 步长为2的行的倒数第二列
print(ndarr[::2,-2])
print('--------------------')
#、索引
arr=np.arange(10)
ndarr=np.arange(16).reshape((4,4))
print(arr)
print(ndarr)
print(arr[1])
print(ndarr[1,1])
# 第2行的第1、2列元素
print(ndarr[2,[1,2]])
# 前3行的第0、1列元素
print(ndarr[:3,[0,1]])
print('--------------------------------')

#布尔索引
cities=np.array(['bj','cd','sh','gz','cd'])
print(cities)
data=np.arange(20).reshape(5,4)
print(data)

print(cities=='cd')
#cd的索引为1和4
print(data[cities=='cd'])
print(data[cities=='cd',:1])
print(cities !='cd')
print(data[cities !='cd'])
print(data[cities !='cd',:1])
print('--------------------------------')
#花式索引 —— 指的是利用整数数组进行索引
arr3=np.arange(36).reshape(6,6)
print(arr3)
# 取出第3，4, 5行
print(arr3[[3,4,5]])
# 使用负数索引将会从末尾开始选取行
print(arr3[[-4,-2,-1]])
# 取出下标为(1, 1), (2, 2), (3, 3)的元素
print(arr3[[1,2,3],[1,2,3]])
# 同时在行和列上进行花式索引
#第1，2，3行 第1，2，3列
print(arr3[[1,2,3]] [:,[1,2,3]])