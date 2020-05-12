import tensorflow as tf

a=tf.ones([1,3])
b=tf.fill([1,3],3.)
print(a)
print(b)
print(tf.add(a,b))
print(tf.subtract(a,b))
print(tf.multiply(a,b))
print(tf.divide(b,a))