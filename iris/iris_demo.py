#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/4/3 16:00
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

print(iris.data, iris.target)
from sklearn import svm
from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)
# clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
# print(clf.score(X_test, y_test))
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
print(clf.predict(digits.data[-1:]))