#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/4/4 9:03
import numpy as np
arr1 = np.array([1,2,3])
print(arr1)
arr2 = np.array([(1,2),(3,4)])
print(arr2)
arr3 = np.zeros((2,3))
print(arr3)
arr4 = np.identity(4)
print('4维单位矩阵',arr4)
arr5 = np.random.random(size=(2,3))
print(arr5)
arr6 = np.arange(5,20,3)
print(arr6)
arr7 = np.linspace(0, 3, 9)
print('arr7:', arr7)
print(arr2.shape)
print(arr2.ndim)# 返回维度
print(arr2.size)# 返回矩阵元素数量
print(arr2.dtype.name) # 返回元素数据类型

def f(x,y):
    return x*10+y

arr8 = np.fromfunction(f, (4,3), dtype=int)
print(arr8)
s1 = [[1,2],[2,1]]
s2 = np.array(s1)
print(s2)
s3 = np.dot(s2,s2)
print(s3)
print('--------------华丽的分隔符------------')
data = np.arange(10).reshape(2,5)
data2 = data.T
print(data2)
print(data)
s4 = np.dot(data2, data)
print(s4)
print(s4.sum(), s4.max(), s4.min())
print(s4.cumsum(axis=1)) # 按行累计求和

print('***********华丽的分割线************')
n1 = np.vstack((s2,s3)) # 纵向合并数组
n2 = np.vsplit(n1,2)
print(n1,'\n', n2)
n3 = np.hstack((s2,s3)) # 横向合并数组
n4 = np.hsplit(n3,2)
print(n3, '\n', n4)