

import numpy as np
'''
矩阵运算   

读取matrixA.txt and matrixB.txt   

进行矩阵乘法运算    

由大到小排序后输出   

numpy   
'''


with open("data/matrixA.txt","r") as lines:
    matrixA=lines.read().split(',')
    '''
       map(function,iterable,...)会根据提供的函数对指定序列做映射.
       第一个参数function以参数序列中的每一个元素调用function函数，返回包含每次function函数返回值的新列表
       iterable--一个或多个序列
       int()函数用于将一个字符串或数字转换为整型。
       list() 方法用于将元组转换为列表
       '''
    matrixA=list(map(int,matrixA))
with open("data/matrixB.txt","r") as lines:
    matrixB=lines.readlines()
    #strip()用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    matrixB=[line.strip() for line in matrixB]
    matrixB=[list(map(int,line.split(','))) for line in matrixB]
    A=np.array(matrixA)
    B=np.array(matrixB)

    C=A.dot(B)
    '''
numpy.sort()
numpy.sort() 函数返回输入数组的排序副本。函数格式如下：

numpy.sort(a, axis, kind, order)
参数说明：

a: 要排序的数组
axis: 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序， axis=0 按列排序，axis=1 按行排序
kind: 默认为'quicksort'（快速排序）
order: 如果数组包含字段，则是要排序的字段
    '''
    C=np.sort(C)


    '''
       savetxt() 函数是以简单的文本文件格式存储数据
       np.savetxt(FILENAME, a, fmt="%d", delimiter=",")
       参数 delimiter 可以指定各种分隔符、针对特定列的转换器函数、需要跳过的行数等。
       a为要保存的矩阵
    '''
    np.savetxt("ans_one.txt",C, fmt="%d")



