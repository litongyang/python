# coding=utf-8
from sklearn.model_selection import train_test_split
import sklearn.linear_model as linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd
import pickle


class ModelPredict:
    def __init__(self):
        self.train_x_man = []
        self.train_y_man = []
        self.train_x_woman = []
        self.train_y_woman = []
        self.data_excel = "novel_data.xls"
        self.data_woman_txt = "data_woman.txt"


    def get_train(self):
        """
        获取训练集
        :return:
        """
        data_man = pd.read_excel(self.data_excel, sheet_name=u"男性", encoding='utf-8')
        data_woman = pd.read_excel(self.data_excel, sheet_name=u"女性", encoding='utf-8')
        x_man = data_man[u'男性小说字数']
        y_man = data_man[u'男性小说收益数']
        x_woman = data_woman[u'女性小说字数']
        y_woman = data_woman[u'女性小说收益']
        for i in x_man:
            one = [int(i)]
            self.train_x_man.append(one)
        for i in y_man:
            one = [round(float(i), 2)]
            self.train_y_man.append(one)
        for i in x_woman:
            one = [int(i)]
            self.train_x_woman.append(one)
        for i in y_woman:
            one = [round(float(i), 2)]
            self.train_y_woman.append(one)
        print self.train_x_woman


    @staticmethod
    def model_predict(train_x, train_y, degree, name_png, title):
        """
        模型训练
        :return:
        """
        X_train, X_test, Y_train, Y_test = train_test_split(train_x, train_y, test_size=0.3, random_state=0)
        """模型训练"""

        ployfeat = PolynomialFeatures(degree=degree)
        x_p_train = ployfeat.fit_transform(X_train)
        clf = linear_model.LinearRegression()
        model = clf.fit(x_p_train, Y_train)
        x_p_test = ployfeat.fit_transform(X_test)
        ypre = model.predict(x_p_test)
        # """评估模型"""
        print "平均绝对误差:", mean_absolute_error(Y_test, ypre)  # 平均绝对误差
        print "方差得分:", explained_variance_score(Y_test, ypre)  # 方差得分
        print "均方差:", mean_squared_error(Y_test, ypre)  # 均方差
        print "判定系数", r2_score(Y_test, ypre)  # 判定系数
        with open('clf.pickle', 'wb') as f:
            pickle.dump(model, f)
        """画图"""
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'
        plt.scatter(X_test, ypre)
        plt.plot(X_test, ypre, c='blue')
        plt.xlabel(u'小说字数')
        plt.ylabel(u'小说收藏数')
        plt.title(title + u"小说字数和收益数关系模型")
        plt.savefig(name_png + '.png', dpi=600)
        plt.show()


if __name__ == '__main__':
    modelPredict = ModelPredict()
    modelPredict.get_train()
    modelPredict.model_predict(modelPredict.train_x_man, modelPredict.train_y_man, 5, "man_profit", u"男性")
    modelPredict.model_predict(modelPredict.train_x_woman, modelPredict.train_y_woman, 3, "woman_profit", u"女性")
