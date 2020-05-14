import tensorflow as tf
import numpy as np

SEED=23455

rdm=np.random.RandomState(seed=SEED)#生成[0,1)之间的随机数
x=rdm.rand(32,2)# 32行2列的输入特征x
# 生成噪声[0,1)/10=[0,0.1); [0,0.1)-0.05=[-0.05,0.05)
y_=[[x1+x2+(rdm.rand()/10.0-0.05)] for (x1,x2) in x]
x=tf.cast(x,dtype=tf.float32)#x转变数据类型
w1=tf.Variable(tf.random.normal([2,1],stddev=1,seed=1))
epoch=15000
lr=0.002
for epoch in range(epoch):
    with tf.GradientTape() as tape:
        y=tf.matmul(x,w1)#前向传播计算结果y
        loss_mse=tf.reduce_mean(tf.square(y_ -y))
    grads=tape.gradient(loss_mse,w1)#损失函数对w1求偏导
    w1.assign_sub(lr*grads)#更新参数w1
    if epoch%500==0:
        print("After %d training steps,w1 is " %(epoch))
        print(w1.numpy(),"\n")
print("Final w1 is: ",w1.numpy()) #1.00x1+1.00x2