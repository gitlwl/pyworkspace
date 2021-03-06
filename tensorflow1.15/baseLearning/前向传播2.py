import tensorflow as tf

#定义输入参数
#用placeholder实现输入定义(sess.run中喂一组数据)
x=tf.placeholder(tf.float32,shape=(1,2))#一组数据，2两个特征
w1=tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2=tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))
#定义前向传播
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)
#用会话计算结果
with tf.Session() as sess:
    init_op=tf.global_variables_initializer()
    sess.run(init_op)
    print("y is :\n",sess.run(y,feed_dict={x:[[0.7,0.5]]}))