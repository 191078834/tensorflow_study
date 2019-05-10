#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/4/10 10:33
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
xx, yy = np.meshgrid(np.linspace(0,10,10), np.linspace(0,100,10))
print(xx)
zz = 4.0*xx + 8.5*yy + np.random.randint(0,100,(10,10))# 0-100 10r10c
# 把一维数组按列排列成多维数组。但是该函数只能适用于numpy对象，即array或者mat，普通的list列表是不行的
# 就是有一个特征向量转换为两个特征向量 ***不负责任的说法***
X, Z = np.column_stack((xx.flatten(), yy.flatten())), zz.flatten()
print(X)
print('***')
print(Z)
line = LinearRegression()
line.fit(X, Z)
# 获取系数与截距
a,b = line.coef_, line.intercept_
x = np.array([[5.8,78.6]])
print('实际值:',np.sum(a*x)+b)
print('预测值:',line.predict(x))
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(xx, yy, zz)
print(line.predict(X).reshape(10,10))
ax.plot_wireframe(xx, yy, line.predict(X).reshape(10,10))
ax.plot_surface(xx, yy, line.predict(X).reshape(10,10), alpha=0.3)
plt.show()
