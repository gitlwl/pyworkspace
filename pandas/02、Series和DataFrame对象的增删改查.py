import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame

# 查

data = [1, 2, 3]
index = ['a', 'b', 'c']
s = Series(data=data, index=index)
print(s)
print(s['b'])
# 范围，左闭右开，返回Series切片
print(s[0:2])
# 注意，利用标签切片的时候左右都是闭区间
print(s['a':'c'])
# 列表，返回Series切片
print(s[[0, 2]])
print(s[['a', 'c']])

# mask，类似于列表，只是长度必须和Series相同，返回Series切片
mask = [False, True, False]
print(s[mask])

'''
1.1.2 .loc[]基于索引
.loc[]查询方式和[]完全一致。
'''
print(s.loc['b'])
print(s['b'])

# 范围，注意：左闭右闭，返回Series切片
print(s.loc['a':'c'])
print(s[0:3])
# 列表，返回Series切片
print(s.loc[['a', 'c']])
# mask，和iloc[]效果等同，返回Series切片
mask = [True, True, False]
print(s.loc[mask])
'''
1.1.3 .iloc[]，基于位置
无视索引，只安装位置定位。
'''
print(s.iloc[1])
print(s[1])
# 范围，左闭右开，返回Series切片
print(s.iloc[0:2])
# 列表，返回Series切片
print(s.iloc[[0, 2]])
# mask，类似于列表，只是长度必须和Series相同，返回Series切片
mask = [False, True, False]
print(s.iloc[mask])

print('------1.2 改------1.2.1 改值---')
# 深copy，拷贝数据结构包含的所有信息
s1 = s.copy()
s1['a'] = 10
s1['b'] = 10
print(s1)
s1[0:2] = 10
print(s1)
'''
函数修改：Series.replace(to_replace=None, value=None, inplace=False)
to_replace：要修改的值，可以为列表
value：改为的值，可以为列表，与to_repalce要匹配；
inplace：是否在原地修改；
'''
print(s1.replace(to_replace=10, value=100, inplace=False))
'''
1.2.2 改索引
直接在index上改，index类似于tuple，
只能引用到别处，不能切片修改
'''
s1 = s.copy()
s1.index = ['a', 'e', 'f']
print(s1)
'''
函数修改：Series.rename(index=None, level = None, inplace = False)
index：list or dict，list时必须和已有索引长度相同，dict可以部分修改；
level：多重索引时，可以指定修改哪一重，从0开始递增；
inplace：是否原地修改。
'''
print(s1.rename(index={'e': 'b'}, inplace=False))

'''
1.3 增

'''
# 1.3.1 直接增一行
s1 = s.copy()
s1['d'] = 4
print(s1)
'''
1.3.2 函数增多行
Series.append(to_append, ignore_index=False, verify_integrity=False)
to_append: 另一个series或多个Series构成的列表；
ignore_index：False-保留原有索引，True-清除所有索引，生成默认数值索引；
verify_integrity：True的情况下，如果to_append索引与当前索引有重复，则报错。
'''
s1 = pd.Series([22, 33], index=['a', 'g'])
print(s.append(s1, ignore_index=False))

print('-----删------')
# 直接删一行
s = Series(np.arange(4), index=['a', 'b', 'c', 'd'])
s2 = s.drop('c')
print(s2)
'''
1.4.2 函数删多行
Series.drop(labels, level=None, inplace=False)
labels：索引，单索引或索引的列表；
level：多重索引需要设置；
inplace：是否本地修改。
'''
s1 = s.copy()
print(s1.drop(['a', 'c']))

print('----DataFrame-----')

data = [[1, 2, 3], [4, 5, 6]]
index = ['a', 'b']
columns = ['A', 'B', 'C']
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)

'''
2.1.1 []，快捷查看
[] 属于快捷查看方式，只包含下面四种，两种列操作、两种行操作。
'''
# 索引是列操作，切片是行操作，一维布尔索引是行操作
# 列操作，单列索引，返回Series。相当于 df.A。
print(df['A'])
# 列操作，列索引列表，返回DataFrame
print(df[['A', 'C']])

# 行操作，位置范围，返回DataFrame
print(df[:1])
# 行操作，mask，必须和行长度一致，返回DataFrame
mask = [False, True]
print(df[mask])
print(df['a':'b'])
print(df[df > 5])
'''
2.1.2 .loc[]，基于索引
.loc[]在DataFrame中与[]不一致。
DataFrame 有两维，每一维都和 Series 的 .loc[] 用法相同；
Series有四种方式，所以DataFrame有16种方式;
可以缺省后面维度，默认补全为 ':' 
'''
# 返回单一值，因为两维都是单索引
print(df.loc['b', 'B'])
# 返回Series，如果只有一维是单索引
print(df.loc['a':'b', 'A'])
# 返回Series，如果只有一维是单索引
print(df.loc[['a', 'b'], 'B'])

mask1 = [True, False]
print(df.loc[mask1, 'B'])

print('-----2.1.3 .iloc[]，基于位置------')
# 返回单一值，因为两维都是scalar
print(df.iloc[1,1])
# 返回Series，如果只有一维是scalar
print(df.iloc[0:2,0])

# 返回DataFrame
print(df.iloc[[0,1],[0,2]])
# 返回DataFrame
mask1=[False,True,False]
mask2=[True,False]
print(df.iloc[mask2,mask1])

'''
2.2.1 改值
直接在1.1查的基础上赋值进行修改，
.loc[]方法确保在原地修改，否则会报warning。
'''
df1=df.copy()
df1.loc['a','A']=10
print(df1)

'''
函数批量任意修改：DataFrame.replace(to_replace=None, value=None, inplace=False)
to_replace：要修改的值，可以为列表
value：改为的值，可以为列表，与to_repalce要匹配；
inplace：是否在原地修改；
'''
print(df1.replace(to_replace=10,value=100,inplace=False))
#交换两列
df1[['A','B']]=df1[['B','A']]
print(df1)
'''
2.2.2 改索引
直接在索引上改，索引类似于tuple，必须全改，不能切片修改
'''
df1=df.copy()
df1.index=['e','f']
df1.columns=['E','F','G']
print(df1)
'''
函数修改：DataFrame.rename(index=None, columns = None,  level = None, inplace = False)
index：list or dict，list时必须长度相同，dict时可以部分修改；
columns：list or dict，list时必须长度相同，dict时可以部分修改；
level：多重索引时，可以指定修改哪一重，目前还用不着；
inplace：是否原地修改。
'''
print(df1.rename(index={'e':'b'},columns={'E':'A'},inplace=False))
print('--------------------------')

#2.3.1 直接增一行
df1=df.copy()
df1.loc['c']=[7,8,9]
print(df1)
'''
2.3.2 函数增多行
pd.concat(objs, axis=0)
确保 列索引 相同，行增加。 （其实这个函数并不要求列索引相同，它可以选择出相同的列。而我写这个教程遵循了python的宣言—明确：做好一件事有一种最好的方法，精确控制每一步，可以少犯错。）

objs: list of DataFrame；
axis: 取0，进行行增加操作。
'''

df1=DataFrame([[22,33,44],[55,66,77]],index=['c','d'],columns=['A','B','C'])
print(pd.concat([df,df1],axis=0))
#2.3.3 直接增一列
df1=df.copy()
df1['H']=[7,8]
print(df1)
'''
2.3.4 函数增多列
pd.concat(objs, axis=1)
确保行索引相同，列增加

objs: list of DataFrame；
axis: 取1，进行列增加操作。
'''
df1=pd.DataFrame([[22,33],[44,55]],index=['a','b'],columns=['D','E'])
print(pd.concat([df,df1],axis=1))
'''
2.4.1 函数删多行
DataFrame.drop(labels, axis = 0,  level=None, inplace=False)
labels：索引，单索引或索引的列表；
axis：0-删行；
level：多重索引需要指定；
inplace：是否本地修改。
'''
df1=df.copy()
print(df1.drop(['a'],axis=0))

#2.4.2 直接删一列
df1=df.copy()
del df1['A']
print(df1)
'''
2.4.3 函数删多列
DataFrame.drop(labels, axis = 1,  level=None, inplace=False)
labels：索引，单索引或索引的列表；
axis：1-删列；
level：多重索引需要指定；
inplace：是否本地修改。
'''

df1=df.copy()
# axis=1 或 ‘columns’
print(df1.drop(['A','C'],axis=1))
