import numpy as np

arr=np.arange(9).reshape((3,3))
print(arr)
'''
diag(v, k=0)

以一维数组的形式返回方阵的对角线（或非对角线）元素，
或将一维数组转换为方阵（非对角线元素为0）
'''
print(np.diag(arr))
print(np.diag(arr,1))

diag_arr=np.array([1,2,3])
print(np.diag(diag_arr))

# 计算矩阵乘积
a=[[1,0],[0,1]]
b=[[4,1],[2,2]]
print(a)
print(b)

'''
dot(a, b[, out])

两个数组的点积
'''
print(np.dot(a,b))
'''
trace(a[, offset, axis1, axis2, dtype, out])
计算对角线元素的和
'''
print(np.trace(arr))
'''
linalg.det(a)

计算矩阵行列式
'''
arr2=np.array([[1,2],[3,4]])
print(np.linalg.det(arr2))

'''
linalg.inv(a)

计算方阵的逆
'''
print(np.linalg.inv(arr2))