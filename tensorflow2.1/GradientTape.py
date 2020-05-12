import tensorflow as tf

with tf.GradientTape() as tape:
    w=tf.Variable(tf.constant(3.0))
    loss=tf.pow(w,2)
grad=tape.gradient(loss,w)
print(grad)