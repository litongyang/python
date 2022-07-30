# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
"""pca test"""
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
iris = load_iris()
y = iris.target
X = iris.data
#作为数组，X是几维？
print X.shape
#作为数据表或特征矩阵，X是几维？
import pandas as pd
pd.DataFrame(X)
#调用PCA
pca = PCA(n_components=1) #实例化
pca = pca.fit(X) #拟合模型
X_dr = pca.transform(X) #获取新矩阵
print X_dr
#也可以fit_transform一步到位
#X_dr = PCA(2).fit_transform(X)
