#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/5/9 11:20
import tensorflow as tf
a = tf.constant([[1., 2.]])
b = tf.constant([[3.], [4.],])
c = tf.matmul(a, b)

state = tf.Variable(0, name="counter")
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)
print()
with tf.Session() as sess:
    #with tf.device(""):
    result = sess.run(c)
    print(sess.run([output], feed_dict={input1:[7.], input2:[2.]})) # tensor not add [] return tensor
    print(result)