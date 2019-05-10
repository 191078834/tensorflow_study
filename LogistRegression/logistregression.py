#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/4/8 17:00
from sklearn.linear_model import LogisticRegression, RandomizedLogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import math
from io import StringIO
csv_data = 'square_feet,price\n150,6450\n200,7450\n250,8450\n300,9450\n350,11450\n400,15450\n600,18450\n'
# print(csv_data)
# df = pd.read_csv(StringIO(csv_data))
print(math.exp(0.5))