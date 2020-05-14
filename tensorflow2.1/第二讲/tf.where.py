import tensorflow as tf

'''
tf.where()
条件语句真返回A,条件语句假返回B
tf.where(条件语句,真返回A，假返回B)
'''
a=tf.constant([1,2,3,1,1])
b=tf.constant([0,1,3,4,5])
#若a>b，返回a对应位置的元素，否则返回b对应位置的元素
#1>0,2>1,3不大于3,1不大于4，1不大于5
c=tf.where(tf.greater(a,b),a,b)
print("c: ",c )