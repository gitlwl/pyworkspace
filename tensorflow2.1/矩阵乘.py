import tensorflow as tf

a=tf.ones([3,2])
b=tf.fill([2,3],3.)
print(tf.matmul(a,b))