import numpy as np

'''
广播
广播是指不同形状的数组之间的算术运算的执行方式。
受限于某些约束，较小的数组依据较大数组“broadcasting”，
使得它们具有兼容的形状。
广播的原则
如果两个数组的后缘维度（即从末尾开始算起的维度）的轴长度相符或其中一方的长度为1，
则认为它们是广播兼容的。广播会在缺失和（或）长度为1的维度上进行。
'''
arr1=np.arange(24).reshape(3,4,2)
arr2=np.array([[4],
              [4],
               [4],
               [4]])

print(arr1)
print(arr2)

print(arr1 * 3)
print(arr1.shape)
print(arr2.shape)
print(arr1-arr2)

arr3=np.arange(48).reshape((8,1,6,1))
arr4=np.arange(35).reshape((7,1,5))
print(arr3.shape)
print(arr4.shape)
print(arr3-arr4)
