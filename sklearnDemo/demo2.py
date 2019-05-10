#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/5/6 11:31
import tensorflow.examples.tutorials
from collections import Counter
import numpy as np
batch = np.ndarray(shape=(8), dtype=np.int32)
labels = np.ndarray(shape=(8, 1), dtype=np.int32)
print(batch)
print(labels)
for i in range(4):
    context_words = [w for w in range(3) if w != 1]
    print(context_words)
print(17005211%17005207)