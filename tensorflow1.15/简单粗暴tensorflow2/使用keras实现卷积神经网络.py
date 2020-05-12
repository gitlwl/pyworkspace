import tensorflow as tf
import numpy as np


class CNN(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.conv1=tf.keras.layers.Conv2D(
            filters=32,
            kernel_size=[5,5],
            padding='same',
            activation=tf.nn.relu
        )