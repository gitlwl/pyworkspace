import tensorflow as tf

IMAGE_SIZE = 28
NUM_CHANNELS = 1
CONV1_SIZE = 5 #第一层卷积核大小
CONV1_KERNEL_NUM = 32 #第一层使用32个卷积核
CONV2_SIZE = 5
CONV2_KERNEL_NUM = 64
FC_SIZE = 512 #第一层全连接网络512个神经元
OUTPUT_NODE = 10#第二层全连接网络10个神经元


def get_weight(shape, regularizer):
    #shape生成张量的维度
    w = tf.Variable(tf.truncated_normal(shape, stddev=0.1))
    if regularizer != None: tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(regularizer)(w))
    return w


def get_bias(shape):
    b = tf.Variable(tf.zeros(shape))
    return b


def conv2d(x, w):
    #x 输入图片x(输入描述) 四阶张量
    #w 对卷积核的描述 四阶张量
    #strides卷积核滑动步长
    return tf.nn.conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    # x 输入图片x(输入描述) 四阶张量
    # ksize池化核大小
    # strides卷积核滑动步长
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


def forward(x,train,regularizer):
    conv1_w=get_weight([CONV1_SIZE,CONV1_SIZE,NUM_CHANNELS,CONV1_KERNEL_NUM],regularizer)
    conv1_b=get_bias([CONV1_KERNEL_NUM])
    conv1=conv2d(x,conv1_w)
    relu1=tf.nn.relu(tf.nn.bias_add(conv1,conv1_b))
    pool1=max_pool_2x2(relu1)

    conv2_w = get_weight([CONV2_SIZE, CONV2_SIZE, CONV1_KERNEL_NUM,CONV2_KERNEL_NUM], regularizer)
    conv2_b = get_bias([CONV2_KERNEL_NUM])
    conv2 = conv2d(pool1, conv2_w)
    relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_b))
    pool2 = max_pool_2x2(relu2)

    pool_shape=pool2.get_shape().as_list()
    #提取特征的长度，宽度，深度
    nodes=pool_shape[1] * pool_shape[2]*pool_shape[3]
    reshaped=tf.reshape(pool2,[pool_shape[0],nodes])

    fc1_w=get_weight([nodes,FC_SIZE],regularizer)
    fc1_b=get_bias([FC_SIZE])
    fc1=tf.nn.relu(tf.matmul(reshaped,fc1_w)+fc1_b)
    if train: fc1 =tf.nn.dropout(fc1,0.5)

    fc2_w = get_weight([FC_SIZE,OUTPUT_NODE], regularizer)
    fc2_b = get_bias([OUTPUT_NODE])
    y=tf.matmul(fc1,fc2_w)+fc2_b
    return y

