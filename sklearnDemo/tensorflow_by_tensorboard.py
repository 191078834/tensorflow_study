#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/5/9 15:41
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

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

x_data = np.linspace(-1,1,300)[:,np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
print(noise)
y_data = np.square(x_data)-0.5 + noise

with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32,[None,1], name='x_input')
    ys = tf.placeholder(tf.float32,[None,1], name='y_input')

l1 = add_layer(xs, 1, 10, 1, activation_function=tf.nn.relu)
prediction = add_layer(l1, 10, 1, 2, activation_function=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),
            reduction_indices=[1]), name='loss')
    tf.summary.scalar('loss', loss)
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
# init2 = tf.initialize_all_variables()
sess = tf.Session()
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter('logs/', sess.graph)

init = tf.global_variables_initializer()
sess.run(init)
# for i in sess.run(l1, feed_dict={xs: x_data, ys: y_data}):
#     print(i)
for i in range(2000):
    sess.run(train_step, feed_dict={xs: x_data, ys:y_data})
    if i%100:
        result = sess.run(merged, feed_dict={xs:x_data, ys:y_data})
        writer.add_summary(result, i)