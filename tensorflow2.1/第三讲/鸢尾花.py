import tensorflow as tf
from sklearn import datasets
import numpy as np
#tain test
x_train=datasets.load_iris().data
y_train=datasets.load_iris().target
#数据集的乱序
np.random.seed(116)
np.random.shuffle(x_train)
np.random.seed(116)
np.random.shuffle(y_train)
tf.random.set_seed(116)
#models.Sequential     3：神经元个数
model=tf.keras.models.Sequential([
    tf.keras.layers.Dense(3,activation='softmax',kernel_regularizer=tf.keras.regularizers.l2())
])
#model.compile
model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.1),
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy'])
#model.fit  validation_split=0.2告知从训练集中选择20%的数据作为测试集
model.fit(x_train,y_train,batch_size=32,epochs=500,validation_split=0.2,validation_freq=20)
#model.summary
model.summary()