#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/4/4 16:29

import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
import numpy as np
boston = load_boston()
x = boston.data[:,np.newaxis, 5] #以每个元素对应一个列表返回数据集指定的第６列
y = boston.target
print(y)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(x,y)
print(lm.score(x,y))
plt.scatter(x, y, color='blue')
plt.plot(x, lm.predict(x), color='red', linewidth=3)
plt.xlabel('feature')
plt.ylabel('price')
plt.title('2D demo')
print(x,lm.predict(x))
plt.show()
# print(y)

