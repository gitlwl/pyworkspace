import tensorflow as tf

w=tf.Variable(tf.constant(5,dtype=tf.float32))
lr= 0.2
epoch=40
for epoch in range(epoch):#for epoch定义顶层循环，表示对数据集循环epoch次，此例数据集仅有1个w，初始化constant赋值为5，循环40次迭代
    with tf.GradientTape() as tape:#with结构到grads框起了梯度的计算过程
        loss=tf.square(w+1)
    grads=tape.gradient(loss,w) #.gradient函数告知谁对谁求导

    w.assign_sub(lr * grads)#assign_sub对变量做自减,即w-=lr*grads即w=w-lr*grads
    print("After %s epoch,w is %f,loss is %f" %(epoch, w.numpy(),loss))