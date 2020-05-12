import tensorflow as tf

w=tf.Variable(4)
w.assign_sub(1)
print(w)