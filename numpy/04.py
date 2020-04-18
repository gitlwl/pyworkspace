import numpy as np

'''
完全不拷贝
一个数组的任何变化都反映在另一个数组上，包括值变化和形状变化
'''
a=np.arange(12)
b=a
print(a)
print(b)
b[5]=500
print(a)
print(b)
print(b is a)

b.shape=(2,6)
print(a)
print(b)
print('--------------------------------------------------------')
'''
浅拷贝
一个数组值会变化会反映在另一个数组上，但是形状不变化
'''
a=np.arange(12)
c=a.view()
print(a)
print(c)
print(c is a)
print(c.base is a)

c[2]=200
print(a)
print(c)
c.shape=(12,1)
print(a)
print(c)
print('-----------------------------------')
'''
深拷贝

创建原数组的副本，副本的任何变化都不会反映在原数组上
'''
a=np.arange(12)
d=a.copy()
print(a)
print(d)
print(d is a)

a[1]=100
print(a)
print(d)
d.shape=(12,1)
print(a)
print(d)