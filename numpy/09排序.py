import numpy as np

arr1=np.random.randn(10)
print(arr1)

'''
sort(a[, axis, kind, order])
返回数组的排序副本
'''
print(np.sort(arr1))

'''
ndarray.sort([axis, kind, order])
就地对数组进行排序
'''
# 就地进行排序，修改原数组
arr1.sort()
print(arr1)

print('-------多维数组排序-----------')
arr2=np.random.randn(3,4)
print(arr2)
# 按列排序
print(np.sort(arr2,axis=1))
# 按行排序
print(np.sort(arr2,axis=0))
# 按关键字排序
my_dt=np.dtype([('name','U10'),('age',int)])
print(my_dt)

#按键排序

arr3=np.array([("罗志祥",21),("黄渤",25),("孙红雷",17),("黄磊",27)],dtype=my_dt)
print(arr3)
print(np.sort(arr3,order='age'))