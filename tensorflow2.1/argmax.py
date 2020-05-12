import tensorflow as tf
import numpy as np

test = np.array([[1, 2, 3], [2, 3, 4], [5, 4, 3], [8, 7, 2]])
print(test)
print(tf.argmax(test, axis=0))
print(tf.argmax(test, axis=1))
