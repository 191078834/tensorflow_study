#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/4/4 11:43
from scipy import poly1d
p = poly1d([3,4,5])
print(p)
p2 = p.deriv()

print(p2)
print(p2([1]), type(p2[1]))

# 函数向量化
import numpy as np
def addsubtract(a,b):
    if a>b:
        return a+b
    else:
        return a-b
vec_addsubtract = np.vectorize(addsubtract)
print(vec_addsubtract([0,3,6], [1,3,5]))