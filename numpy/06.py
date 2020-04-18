import numpy as np

arr=np.array([[np.NaN,0,1,2,3],
              [4,5,np.NaN,6,7],
              [8,9,10,np.NaN,11]])
print(arr)
print(np.amax(arr))
#返回数组的最大值或沿轴方向的最大值，忽略任何NAN
#默认是计算flatten之后的数组，可以指定axis参数 0/1
print(np.nanmax(arr))
#返回数组的最小值或沿轴的最小值，忽略任何NAN
print(np.nanmin(arr))
# 平均值
print(np.nanmean(arr))
# 中位数 在忽略NAS的情况下，沿指定的轴计算中值
print(np.nanmedian(arr))
# 标准差
print(np.nanstd(arr))
# 方差
print(np.nanvar(arr))
#布尔值True和False会被转为1和0参与计算
bool_arr=np.array([0.7,0,0.5,True,False,True,True,True,False,True])
print(bool_arr.sum())

arr2=np.array([0.1,0.2,0.3,True,False])
print(np.amax(arr2))
print(np.amin(arr2))