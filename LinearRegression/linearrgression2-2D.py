#!/usr/bin/python
# -*- coding: utf-8 -*-
#Auther: WQM
#Time: 2019/4/10 9:12
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
csv_data = 'square_feet,price\n150,6450\n200,7450\n250,8450\n300,9450\n350,11450\n400,15450\n600,18450\n'
#print(csv_data)
df = pd.read_csv(StringIO(csv_data))
#print(df)
line = LinearRegression()
# print(df['square_feet'].values.reshape(-1,1))
line.fit(df['square_feet'].values.reshape(-1,1),df['price'])
a,b = line.coef_, line.intercept_  # 获取直线的斜率与截距
print(a,b)
area = 258
print(a*area+b)
print(line.predict([[area]]))
print('*********')
plt.scatter(df['square_feet'], df['price'])
plt.plot(df['square_feet'], line.predict(df['square_feet'].values.reshape(-1,1)), color='yellow', linewidth=5)
plt.show()