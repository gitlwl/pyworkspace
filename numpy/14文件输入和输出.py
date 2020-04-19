import numpy as np
from io import BytesIO

arr=np.arange(12).reshape(3,4)
print(arr)
print(np.save('file/io',arr))
print(np.load('file/io.npy'))
print(np.savetxt('files/io2',arr))
print(np.savetxt('files/io2',arr,delimiter=','))
print(np.loadtxt('files/io2',delimiter=','))




'''
二进制文件

load(files[, mmap_mode, allow_pickle, …])

从.npy，.npz或pickle文件加载数组或pickle对象

save(files, arr[, allow_pickle, fix_imports])

将数组保存为NumPy .npy格式的二进制文件

savez(files, *args, **kwds)

将多个数组以未压缩的.npz格式保存到单个文件中

savez_compressed(files, *args, **kwds)

将多个数组以压缩的.npz格式保存到单个文件中

文本文件

loadtxt(fname[, dtype, comments, delimiter, …])

从文本文件加载数据

savetxt(fname, X[, fmt, delimiter, newline, …])

从文本文件加载数据

genfromtxt(fname[, dtype, comments, …])

从文本文件加载数据，并按指定处理缺失值

fromregex(files, regexp, dtype[, encoding])

使用来自文本文件构造数组
'''



