import numpy as np

int_arr=np.arange(6).reshape(2,3)
print(int_arr)
print('类型信息:',int_arr.dtype)
var_float16=np.float16([12,121])
print(var_float16)
print(var_float16.dtype)
float_arr=int_arr.astype(np.float32)
print('astype()转换数据类型：',float_arr)

float_arr2=np.array([1.2,2.6,3.5,4.9,5.0])
print(float_arr2)
print(float_arr2.astype('int'))
str_arr=np.array(['2.001','1.25','88','-236.123','00'],dtype=np.string_)
print(str_arr)
print(str_arr.astype('float'))
print('查看所有的父类：',np.int32.mro())

print('判断类型：',np.issubdtype(float_arr.dtype,np.floating))
print('判断类型：',np.issubdtype(np.int32,np.floating))

my_dtype=np.dtype([('name','S10'),('age',int),('city','S10')])
print('自定义类型：',my_dtype)
temp_arr=[('zhangsan',20,'BJ'),('lisi',22,'CD'),('wangwu',21,'SH')]
my_arr=np.array(temp_arr,dtype=my_dtype)
print(my_arr)

print(my_arr[1])
print(my_arr['name'])