import numpy as np

data=[[1,2,3],[4,5,6]]
arr1=np.array(data)
print(arr1)
arr2=np.asarray(arr1)
print(arr2)
arr3=np.zeros([3,4])
print(arr3)
arr4=np.zeros_like(data)#数组作为参数
print(arr4)
arr5=np.ones([2,3])
print(arr5)
arr6=np.ones_like(data)#数组作为参数
print(arr6)
arr7=np.empty([2,2])
print(arr7)
arr8=np.empty_like(data)
print(arr8)

arr9=np.full([2,3],fill_value=3)
print("根据指定形状传建一个ndarray对象，"
      "并用fill_value的值进行填充",arr9)
arr10=np.full_like(data,8)
#传入一个数组作为参数，根据该数组的形状创建一个ndarray对象，
# 并用fill_value的值进行填充
print(arr10)

arr11=np.identity(5)
#传入一个整数N，创建一个N * N的单位矩阵
print(arr11)

arr12=np.eye(5)
print(arr12)

arr13=np.random.randn(2,3)
print(arr13)

arr14=np.arange(start=0,stop=10,step=2)
'''
参数
start：开始位置，数字，可选，默认值为0
stop：结束位置，数字，
step：步长，数字，可选，默认为1。如果指定step则必须指定start
dtype：类型。不指定则自动推断
'''
print(arr14)

arr15=np.linspace(0,10,5)
#返回指定间隔内的等距数字。
print(arr15)

def fun(x,y):
    return x * 20 +y
#通过对每个坐标执行函数来构造数组
#4行6列
result=np.fromfunction(fun,(4,6),dtype=np.int)
print(result)
def my_dot(a,b):
    return a * b
result2=np.fromfunction(my_dot,(2,3))
print(result2)

print(np.fromfunction(lambda i,j:i+j,(2,3)))

'''
np.fromfile(files, dtype=float, count=-1, sep='')

files：要打开的文件对象或者文件名
dtype：返回数组的数据类型。对于二进制文件，
它用于确定文件中项目的大小和字节顺序。
错误的数据类型会返回错误的数据
count：要读取的项目数。-1表示所有项目（即完整文件）
sep：如果文件是文本文件，
则表示分隔项之间的分隔符。
空（“”）分隔符表示应将文件视为二进制文件。
分隔符中的空格（“”）与零个或多个空白字符匹配。
仅由空格组成的分隔符必须至少与一个空格匹配
'''
print(np.fromfile('./file/fromfile'))

print(np.arange(12).tofile('./files/fromfile'))