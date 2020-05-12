import tensorflow as tf

x = tf.Variable(initial_value=3.)
with tf.GradientTape() as tape:
    y = tf.square(x)
y_grad = tape.gradient(y, x)
print([y, y_grad])
print('-----------------------')
X = tf.constant([[1., 2.], [3., 4.]])
y = tf.constant([[1.], [2.]])
w = tf.Variable(initial_value=[[1.], [2.]])
b = tf.Variable(initial_value=1.)
with tf.GradientTape() as tape:
    L = 0.5 * tf.reduce_sum(tf.square(tf.matmul(X, w) + b - y))
w_grad, b_grad = tape.gradient(L, [w, b])
print(L.numpy(), w_grad.numpy(), b_grad.numpy())
