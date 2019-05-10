#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/4/4 13:18
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,6), num='统计图', facecolor='yellow')
plt.plot(x,y,'-.', color='black', linewidth=1, label='$sin(x)$')
plt.plot(x,z, ':',color='red', linewidth=1,label='$cos(x^2)$')
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title(u'统计图')
# plt.ylim(-12,12)
plt.legend(loc='best', fontsize='small')
plt.legend(loc='best', fontsize='small').get_frame().set_facecolor('black') # 设置图例背景为红色

plt.subplot(3,1,1)
plt.subplot(2,2,3)
plt.subplot(2,2,4)
plt.show()


