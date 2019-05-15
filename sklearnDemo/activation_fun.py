#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/5/14 13:59
import tensorflow as tf
import math
a = tf.constant([[1.0, 2.0], [2.0, 3.0], [1.0, 3.0]])
sess = tf.Session()

## sigmoid 函数 #
print(sess.run(tf.sigmoid(a)), sess.run(a))
print(1/(math.exp(-2.0)+1))
print('***************************************')

## tanh 函数 #
print(sess.run(tf.tanh(a)), sess.run(a))
print((1-math.exp(-2*1.0))/(1+math.exp(-2*1.0)))
print('****************************************')

## tf.nn.relu 和 tf.nn.softplus 可以看作是relu的平滑版本
## 随着训练的进行，部分输入会落到硬饱和区，导致对应的权重无法更新，称为“神经元死亡
print(sess.run(tf.nn.softplus(a)), sess.run(a))
print(math.log(1+math.exp(-1.0)))
print('****************************************')
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)









