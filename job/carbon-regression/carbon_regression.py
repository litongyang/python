# -*- coding: utf-8 -*-
import pandas as pd
import math
<<<<<<< HEAD

from sklearn.model_selection import train_test_split
import sklearn.linear_model as linear_model
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
import pickle
from sklearn.decomposition import PCA
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

=======
from sklearn.model_selection import train_test_split
import sklearn.linear_model  as linear_model
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
import pickle
>>>>>>> f619db7a7381ce9a4c068cde4e76e28165383780
"""
简介：通过测氧传感器输出电势、温度，来预测炉气碳势
"""


class CarbonRegression:
    def __init__(self):
        self.data = pd.read_excel('data.xls', encoding='utf-8')
        self.oxygen_data = ''  # 氧电势数据
        self.temperature = ''  # 温度数据
        self.carbon = ''  # 炉气碳数据
        self.train_x = []
        self.train_y = []

    def data_cleaning(self):
        self.oxygen_data = self.data[111]  # 获取氧电势数据
<<<<<<< HEAD
        self.temperature = self.data.columns.values[1:]  # 获取温度数据
        for i in self.temperature:
            for j in range(0, len(self.data)):
                if not math.isnan(self.data[i][j]):
                    train_one_x = [i, self.oxygen_data[j]]
=======
        # print self.oxygen_data
        self.temperature = self.data.columns.values[1:]  # 获取温度数据
        temp = self.data
        # print self.temperature
        for i in self.temperature:
            for j in range(0, len(self.data)):
                if not math.isnan(self.data[i][j]):
                    train_one_x = []
                    # print "i:", i
                    # print self.oxygen_data[j]
                    # print self.data[i][j]
                    train_one_x.append(i)
                    train_one_x.append(self.oxygen_data[j])
>>>>>>> f619db7a7381ce9a4c068cde4e76e28165383780
                    self.train_x.append(train_one_x)
                    self.train_y.append(self.data[i][j])
                    # print "============"
                else:
                    pass
<<<<<<< HEAD
        # print len(self.train_x)
        # print len(self.train_y)
=======
        print len(self.train_x)
        print len(self.train_y)
>>>>>>> f619db7a7381ce9a4c068cde4e76e28165383780

        # self.carbon = temp.drop(columns=111).values  # 获取炉气碳数据
        # print self.carbon

    def train_data(self):
<<<<<<< HEAD
        X_train, X_test, Y_train, Y_test = train_test_split(self.train_x, self.train_y, test_size=0.3, random_state=0)

        # 调用PCA,降维训练
        # pca = PCA(n_components=1)  # 实例化
        # pca_train = pca.fit(X_train)  # 拟合模型
        # X_tran_dr = pca_train.transform(X_train)  # 获取新矩阵
        # X_train_dr = X_tran_dr.tolist()
        #
        # pca_test = pca.fit(X_test)  # 拟合模型
        # X_test_dr = pca_test.transform(X_test)  # 获取新矩阵
        # X_test_dr = X_test_dr.tolist()
        # x_train_pca=[]
        # x_test_pca=[]
        # for i in range(0, len(X_train_dr)):
        #     x_train_pca.append(X_train_dr[i][0])
        # for i in range(0, len(X_test_dr)):
        #     x_test_pca.append(X_test_dr[i][0])
        # print x_train_pca
        # print x_test_pca

        """模型训练"""
        log_reg = linear_model.LinearRegression()
        model = log_reg.fit(X_train, Y_train)
        ypre = model.predict(X_test)
        # print ypre
        # print Y_test

        """评估模型"""
        print "平均绝对误差:", mean_absolute_error(Y_test, ypre)  # 平均绝对误差
        print "方差得分:", explained_variance_score(Y_test, ypre)  # 方差得分
        print "均方差:", mean_squared_error(Y_test, ypre)  # 均方差
        print "判定系数", r2_score(Y_test, ypre)  # 判定系数
=======
        X_train, X_test, Y_train, Y_test =train_test_split(self.train_x, self.train_y, test_size=0.3,random_state=0)
        print X_train
        print Y_test
        log_reg = linear_model.LinearRegression()
        model = log_reg.fit(X_train, Y_train)
        ypre = model.predict(X_test)

        """评估模型"""
        print mean_absolute_error(Y_test, ypre)  # 平均绝对误差
        print explained_variance_score(Y_test, ypre)  # 方差得分
        print mean_squared_error(Y_test, ypre)  # 均方差
        print r2_score(Y_test, ypre)  # 判定系数
>>>>>>> f619db7a7381ce9a4c068cde4e76e28165383780

        """保存模型"""
        with open('clf.pickle', 'wb') as f:
            pickle.dump(model, f)

        """读取模型"""
        with open('clf.pickle', 'rb') as f:
            clf2 = pickle.load(f)
            # 测试读取后的Model
<<<<<<< HEAD
            # print(clf2.predict(X_test))

        """画图"""
        x = []
        y = []
        z = ypre
        for i in range(0, len(X_test)):
            x.append(X_test[i][0])
            y.append(X_test[i][1])
        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(x, y, z, label='predict result curve')
        ax.legend()
        plt.show()
=======
            print(clf2.predict(X_test))


>>>>>>> f619db7a7381ce9a4c068cde4e76e28165383780


if __name__ == '__main__':
    carbon_regression = CarbonRegression()
    carbon_regression.data_cleaning()
    carbon_regression.train_data()
<<<<<<< HEAD
=======
    # print carbon_regression.data
    # print carbon_regression.oxygen_data
    # print carbon_regression.temperature
    # print carbon_regression.carbon
>>>>>>> f619db7a7381ce9a4c068cde4e76e28165383780
