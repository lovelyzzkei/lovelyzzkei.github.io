import tensorflow as tf
import numpy as np

t1 = tf.constant(3.0, tf.float32)
t2 = tf.constant(4.0, tf.float32)

@tf.function
def _add(t1, t2):
    return t1 + t2

t3 = _add(t1, t2)
print(t1)
print(t2)
print(t3)

print(t1.numpy())