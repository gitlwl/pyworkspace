import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame
import xlrd



'''
Series是pandas中暴露给我们使用的基本对象，
它是由相同元素类型构成的一维数据结构，
同时具有列表和字典的特点
'''
data=[1,2,3,4,5]
index=['a','b','c','d','e']
s=Series(data,index=index)
print(s)
print(s.index)

print(s.name)
print(s.values)
print(s.dtype)
print(s.shape)
print('-----------------------------------------------')

'''
1.2 创建
Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

1.2.1 无索引创建
如果 data 为 ndarray(1D) 或 list(1D)，那么其缺少 Series 需要的索引信息
如果提供 index，则必须和data长度相同
如果不提供 index，那么其将生成默认数值索引 range(0, data.shape[0])
'''

data1=np.array([1,2,3])
index1=['a','b','c']
s=pd.Series(data=data1,index=index1)
print(s)

'''
1.2.2 有索引创建
如果 data 为 Series 或 dict ，
那么其已经提供了 Series 需要的索引信息，所以 index 项是不需要提供的
如果额外提供了 index 项，那么其将对当前构建的Series进行覆盖
'''

data2={'a':1,'b':2,'c':3}
index2=['a','b','d']
s=pd.Series(data=data2)
print(s)
print('----------------------------')
'''
2、DataFrame
DataFrame由具有共同索引的Series按列排列构成（2D），
是使用最多的对象，可以将其想象成一个Excel表来处理
'''

data=[[1,2,3],[4,5,6]]
index=['a','b']
columns=['A','B','C']
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)
# 行索引
print(df.index)
# 列索引，与Series的name一个意思
print(df.columns)

print(df.values)
print(df.dtypes)
print(df.shape)
print('-------------------------------------------')


'''
2.2 创建
DataFrame(data=None, index=None, columns=None)
函数由多个参数，对我们有用的主要是：data,index和columns三项
'''
'''
2.2.1 data无 行索引，无 列索引
如果 data 为 ndarray(2D) or list(2D)，那么其缺少 DataFrame 需要的行、列索引信息
如果提供 index 或 columns 项，其必须和data的行 或 列长度相同
如果不提供 index 或 columns 项，那么其将默认生成数值索引range(0, data.shape[0])) 或 range(0, data.shape[1])。
'''

data1=np.array([[1,2,3],[4,5,6]])
index1=['a','b']
columns1=['A','B','C']
df=pd.DataFrame(data1,index=index1,columns=columns1)
print(df)

'''
2.2.2 data无 行索引，有 列索引
如果data为 dict of ndarray(1D) or list(1D)，所有ndarray或list的长度必须相同。且dict的key为DataFrame提供了需要的columns信息，缺失index
如果提供 index 项，必须和list的长度相同
如果不提供 index，那么其将默认生成数值索引range(0, data.shape[0]))
如果还额外提供了columns项，那么其将对当前构建的DataFrame进行 列重索引
'''

data2={'A':[1,4],'B':[2,5],'C':[3,6]}
index2=['a','b']
columns2=['A','B','D']
df=pd.DataFrame(data2)
print(df)

'''
2.3 data有 行索引，有 列索引
如果data为 dict of Series or dict，那么其已经提供了DataFrame需要的所有信息
如果多个Series或dict间的索引不一致，那么取并操作（pandas不会试图丢掉信息），缺失的数据填充NaN
如果提供了index项或columns项，那么其将对当前构建的DataFrame进行 重索引（reindex，pandas内部调用接口）
'''
data3={'A':{'a':1,'b':4},'B':{'a':2,'b':5},'C':{'a':3,'c':6}}
df=pd.DataFrame(data3)
print(df)
print('--------------------------------')

'''
3、由文件创建
3.1 由.csv文件创建
pd.read_csv(filepath_or_buffer, sep=',', header='infer', names=None, index_col=None, encoding=None )

read_csv的参数很多，但这几个参数就够我们使用了：
filepath_or_buffer：路径和文件名不要带中文，带中文容易报错
sep: csv文件数据的分隔符，默认是','，根据实际情况修改
header：如果有列名，那么这一项不用改
names：如果没有列名，那么必须设置header = None， names为列名的列表，不设置默认生成数值索引
index_col：int型，选取这一列作为索引
encoding：根据你的文档编码来确定，如果有中文读取报错，试试encoding = 'gbk'
'''
# csv_df=pd.read_csv('files/csv_test.csv')
# print(csv_df.head())
'''
3.2 由.excel文件创建
pd.read_excel(io, sheetname=0, header=0, index_col=None, names=None)
read_excel的参数很多，但这几个参数就够我们使用了：
header：如果有列名，那么这一项不用改；
names：如果没有列名，那么必须设置header = None， names为列名的列表，不设置默认生成数值索引；
index_col：int型，选取这一列作为索引。
'''
excel_df=pd.read_excel('files/excel_test.xls')
print(excel_df.head())