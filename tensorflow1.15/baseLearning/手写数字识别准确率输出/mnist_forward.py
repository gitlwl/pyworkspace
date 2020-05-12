import tensorflow as tf


#神经网络输入节点为784个，组成一维数组
INPUT_MODE=784
#输出10个数，每个数表示对应的索引号出现的概率
OUTPUT_MODE=10
#隐藏层的节点个数
LAYER1_MODE=500
def get_weight(shape,regularizer):
    w=tf.Variable(tf.truncated_normal(shape,stddev=0.1))
    if regularizer != None: tf.add_to_collection('losses',tf.contrib.layers.l2_regularizer(regularizer)(w))
    return w
def get_bias(shape):
    b=tf.Variable(tf.zeros(shape))
    return b
def forward(x,regularizer):
    #第一层
    w1=get_weight([INPUT_MODE,LAYER1_MODE],regularizer)
    b1=get_bias([LAYER1_MODE])
    y1=tf.nn.relu(tf.matmul(x,w1)+b1)
    #第二层
    w2 = get_weight([LAYER1_MODE,OUTPUT_MODE], regularizer)
    b2 = get_bias([OUTPUT_MODE])
    y = tf.matmul(y1, w2) + b2
    return y

