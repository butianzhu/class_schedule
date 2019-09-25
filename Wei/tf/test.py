from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
node1 = tf.constant(2)
node2 = tf.constant(3)
sum_node = node1 + node2

with tf.Session() as sess:
    print(sess.run([node1,sum_node]))