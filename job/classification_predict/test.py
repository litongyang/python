# -*- coding: utf-8 -*-
import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
import numpy as np

data = pd.read_csv('train_0.dat', header=None, delimiter=",")
data1 = pd.read_csv('train_label.dat', header=None, delimiter="\t")
# print data1

file_name_list = os.listdir('data\\train')
file_name = 'data\\train\\' + str(file_name_list[0])
print file_name
x = []
x_train = []
data2 = pd.read_csv(file_name, header=None, delimiter="\n")
for i in range(0, len(data2.values)):
    one = data2.values[i][0].split(',')
    one = [int(num) for num in one]
    x_train.append(one)

# 调用PCA
pca = PCA(n_components=1)  # 实例化
pca = pca.fit(x_train)  # 拟合模型
X_dr = pca.transform(x_train)  # 获取新矩阵
X_dr = X_dr.tolist()
x_test=[]
for i in range(0, len(X_dr)):
    x_test.append(X_dr[i][0])
print x_test
x.append(x_test)
x.append(x_test)
# print
y=[1,0]
# 也可以fit_transform一步到位
# X_dr = PCA(2).fit_transform(X)

#
clf = LogisticRegression()
clf.fit(x, y)

ages_train = [[20, 10000], [22, 12000], [22, 14000], [25, 17000], [30, 29000]]
net_worths_train = [10000, 12000, 14000, 17000, 29000]

reg = LinearRegression()
reg.fit(ages_train, net_worths_train)
