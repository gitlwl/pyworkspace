import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# 数组与标量的算数运算
print(arr * 2)
print(arr + 2)
# 数组与数组之间的运算
print(arr + arr)
print(arr * arr)
print(arr - arr)
print(arr / arr)

# *=、+=运算会修改原对象，而不是创建新对象
arr *= 2
print(arr)

# shape相同的数组之间比较会生成布尔数组
arr2=arr+1
print(arr2>arr)

# 不同类型的数组计算之后的结果的类型会向上转换为更精确的类型
# （如int类型的数组a和float类型的数组b求和得到c的类型为float，
# 而不是int）
int_arr=np.array([1,2,3])
float_arr=np.array([0.1,0.2,0.3])
res_arr=int_arr + float_arr
print(res_arr.dtype)

# 形状不同的数组之间能否进行计算？
arr1=np.array([1,2,3])
# arr2=np.array([1,2,3,4])
# print(arr1+arr2)

arr3=np.array([[1,2,3],
               [1,2,3]])
print(arr1+arr3)