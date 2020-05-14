'''
np.mgrid[]   .ravel()  np.c_[]  可以生成网格坐标点
np.mgrid[]                                [起始值  结束值)
np.mgrid[起始值：结束值：步长，起始值：结束值：步长,....]
x.ravel()  将x变为一组数组,"把 . 前变量拉直"
np.c_[] 使返回的间隔数值点配对
np.c_[数组1，数组2，...]
'''

import numpy as np

x,y=np.mgrid[1:3:1,2:4:0.5]
grid=np.c_[x.ravel(),y.ravel()]
print("x:",x)
print("y:",y)
print('grid:\n',grid)