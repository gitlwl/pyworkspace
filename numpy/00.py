import numpy as np
arr=[[1,2,3],
     [4,5,6]]
ndarr=np.array(arr)
print(ndarr)
print("数组的轴的个数：", ndarr.ndim)
print("数组的形状：",ndarr.shape)
print("数组中元素的总数：",ndarr.size)
print("数组中元素类型：",ndarr.dtype)
print("数组中每个元素的字节大小：",ndarr.itemsize)

arr2=[1+2j,3+4j,5+6j]
complex_arr=np.array(arr2)
print(complex_arr.dtype)
print("数组的实部：",complex_arr.real,"数组的虚部：",complex_arr.imag)