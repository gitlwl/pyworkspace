import numpy as np

arr=np.arange(12)
arr2=arr.copy()
# order默认为‘C’ ，按列读取。等效于reshape(4, 3)
print(arr.reshape((4,3)))
# 按行读取
print(arr.reshape((4,3),order='F'))
# resize()会修改对象本身
arr2.resize((4,3))
print(arr2)
print('--------------------')
#多维数组重塑
ndarr=arr.reshape(4,3)
print(ndarr)

print(ndarr.reshape(2,6))
print('--------------')
# 重塑为三维度
print(arr.reshape((2,2,3)))
#如果想让自动计算某个轴上的大小，可以传入-1
print(arr.reshape((3,2,-1)))
print('----------扁平化处理------------')
ndarr=np.arange(12).reshape(3,4)
print(ndarr)
# order='C'，按列
print(ndarr.flatten())
# 按行
print(ndarr.flatten(order='F'))

# flatten()返回新对象，ravel()返回视图
ravel_ndarr=ndarr.ravel()
print(ravel_ndarr)

ravel_ndarr[1]=100
print(ndarr)
print('---------数组合并-----------------')
a=np.array([[1,2],[3,4]])
b=np.array([[5,6]])
print(a)
print(b)
'''
concatenate
沿着一条轴连接一组（多个）数组。
除了与axis对应的轴之外，其它轴必须有相同的形状。
'''
print(np.concatenate((a,b),axis=0))
print(b.T)
print(a.shape,b.T.shape)
print(np.concatenate((a,a.T),axis=1))

a=np.array([[1,2,3],
            [4,5,6]])
b=np.array([[10,20,30],
            [40,50,60]])
print(a)
print(b)
'''
vstack、row_stack
以追加行的方式对数组进行连接（沿轴0）
'''
print(np.vstack((a,b)))
print(np.row_stack((a,b)))
'''
hstack
以追加列的方式对数组进行连接（沿轴1）
'''
print(np.hstack((a,b)))
'''
column_stack 类似于hstack，但是会先将一维数组转换为二维列向量
dstack以面向“深度”的方式对数组进行叠加
'''
print(np.column_stack((a,b)))
print(np.dstack((a,b)))

'''
4、数组拆分
split 沿指定轴在指定的位置拆分数组
hsplit、vsplit、dsplit 
split的便捷化函数，分别沿轴0、轴1、轴2进行拆分
'''
split_arr=np.arange(36).reshape(6,-1)
print(split_arr)
print('---------')
a,b,c=np.split(split_arr,3,axis=0)
print(a)
print(b)
print(c)

a,b,c=np.split(split_arr,3,axis=1)
print(a,'---')
print(b,'---')
print(c,'---')
print('------------------')
a,b,c,d = np.split(split_arr,[2,4,5],axis=1)
#索引2，4，5处拆分
print(a)
print(b)
print(c)
print(d)

print('--------5.1 repeat —— 针对元素---------------')

arr=np.arange(4)
print(arr)

print(np.repeat(arr,2))
# 指定每个元素的重复次数
# 0重复2次，1重复3次，2重复4次，3重复5次
print(np.repeat(arr,[2,3,4,5]))
#多维数组repeat
ndarr=np.arange(6).reshape(2,3)
print(ndarr)
#不指定轴会被扁平化
print(np.repeat(ndarr,2))
print(np.repeat(ndarr,2,axis=0))
print(np.repeat(ndarr,2,axis=1))

print('------5.2 tile ———— 针对整个数组----')
print(ndarr)

# 对标量是横向扩展
print(np.tile(ndarr,2))

print(np.tile(ndarr,(1,2)))
print(np.tile(ndarr,(2,3)))

print('-------------------------------------')
'''
6、数组转置和轴对换
转置和轴对换返回的是原对象的视图，不是新对象
'''
arr=np.arange(12).reshape(3,4)
print(arr)
print(arr.T)
print(arr.transpose())

print(arr)
arr.T[:2]=0
print(arr)