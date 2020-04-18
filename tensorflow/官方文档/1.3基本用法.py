import tensorflow as tf


#保证sess.run()能够正常运行
tf.compat.v1.disable_eager_execution()

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])
product = tf.matmul(matrix1, matrix2)

# sess = tf.Session()
# tensorflow 2.0以上版本的函数
sess = tf.compat.v1.Session()
result = sess.run(product)
print(result)
sess.close()
