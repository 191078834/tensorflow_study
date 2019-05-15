#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/5/13 15:36
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
mnist = input_data.read_data_sets('MNIST', one_hot='True')

def add_layer(input, in_size, out_size, n_layer, activation_function=None):
    layer_name = 'layer_name_%s'%n_layer
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
        # 生成*随机变量*的权重矩阵
            Weight = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
            tf.summary.histogram(layer_name + '/weights', Weight)
        with tf.name_scope('biases'):
        # 类似列表 推荐值不为0
            biases = tf.Variable(tf.zeros([1,out_size]) + 0.1, name='b')
            tf.summary.histogram(layer_name + '/biases', biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.add(tf.matmul(input, Weight), biases)
            # tf.summary.histogram(layer_name + '/Wx_plus_b', Wx_plus_b)
        # 默认为非线性方程
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b, )
        tf.summary.histogram(layer_name + '/outputs', outputs)
        return outputs

# define placeholder for input to network
xs = tf.placeholder(tf.float32, [None, 784])
ys = tf.placeholder(tf.float32, [None, 10])

predictions = add_layer(xs, 784, 10, 1,activation_function=tf.nn.softmax)

# the erroe between predicction and real data
cross_entropy = ys * tf.log()






























