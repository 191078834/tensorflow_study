#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/5/13 15:36
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
mnist = input_data.read_data_sets('MNIST', one_hot='True')


xs = tf.placeholder(tf.float32, [])
ys = tf.placeholder(tf.float32, [])