import tensorflow as tf
x=tf.constant([[1,2,3],[2,2,3]])
print(x)
print(tf.reduce_mean(x))
print(tf.reduce_sum(x,axis=1))