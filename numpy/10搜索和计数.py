import numpy as np

arr=np.arange(6).reshape(2,3) + 10
print(arr)

'''
argmax(a[, axis, out])
返回沿轴的最大值的索引
axis默认为None，返回flatten之后的索引
'''
print(np.argmax(arr))
print(np.argmax(arr,axis=0))
print(np.argmax(arr,axis=1))
# argmin类似于argmax
print(np.argmin(arr))
print(np.argmin(arr,axis=1))
print('--------------------------')
arr2=np.array([[10,np.NaN,11,12],
               [13,14,15,np.NaN]])
print(arr2)
# 不会忽略NaN值
print(np.argmax(arr2,axis=0))
print(np.nanargmax(arr2,axis=0))
'''
argwhere(a)
返回按元素分组的非零数组元素的索引。

返回的是元素的坐标
'''
print(np.argwhere(arr>12))
'''
nonzero(a)

返回非零元素的索引

返回数组的元组
'''
print(np.nonzero(arr))
'''
flatnonzero(a)

返回a的展平版本中非零的索引
'''
#等效于 np.nonzero(np.ravel(arr))[0]
print(np.flatnonzero(arr))
print(np.nonzero(np.ravel(arr))[0])

print('----------------------------------------')

'''
where(condition, [x, y])
返回元素，可以是x或y，具体取决于条件
'''
arr3=np.array([1,2,3,4,5])
arr4=np.array(['a','b','c','d','e'])
cond=np.array([True,False,True,False,True])
#cond中为true，对应arr4索引变为arr3中索引值
result=np.where(cond,arr3,arr4)
print(result)
# 将arr3中大于3的全部变为-3
print(np.where(arr3>3,-3,arr3))
# 将arr3中大于3的全部变为该值的相反数
print(np.where(arr3>3,-arr3,arr3))
'''
searchsorted(a, v[, side, sorter])
查找应插入元素以维护顺序的索引
'''
print(np.searchsorted([1,2,3,4,5],3))
print(np.searchsorted([1,2,3,4,5],3,side='right'))
print(np.searchsorted([1,2,3,4,5],[-10,10,2,3]))

'''
extract(condition, arr)
返回满足某些条件的数组元素
'''
print(np.extract(arr>12,arr))
'''
count_nonzero(a[, axis])
计算数组a中的非零值的数量
'''
# 默认axis为None，统计flatten之后的数组
print(np.count_nonzero([[0,1,7,0,0],[3,0,0,2,19]]))
#按列
print(np.count_nonzero([[0,1,7,0,0],[3,0,0,2,19]], axis=0))
#按行
print(np.count_nonzero([[0,1,7,0,0],[3,0,0,2,19]], axis=1))