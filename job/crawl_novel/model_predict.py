# coding=utf-8
from sklearn.model_selection import train_test_split
import sklearn.linear_model as linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt


class ModelPredict:
    def __init__(self):
        self.train_x_man = []
        self.train_y_man = []
        self.train_x_woman = []
        self.train_y_woman = []
        self.data_man_txt = "data_man.txt"
        self.data_woman_txt = "data_woman.txt"

    @staticmethod
    def get_train(file_name, train_x_man, train_y_man):
        """
        获取训练集
        :return:
        """
        data_list = []
        for line in open(file_name):
            line_list = line.split('\t')
            line_list = line_list[0:len(line_list) - 1]
            data_list.append(line_list)
        for i in data_list[0]:
            i = i.split('\t')
            train_x_man.append([int(num) for num in i])
        for j in data_list[1]:
            j = j.split('\t')
            train_y_man.append([int(num) for num in j])
        print "训练数据：", train_x_man
        print "训练label：", train_y_man

    @staticmethod
    def model_predict(train_x, train_y, degree, name_png):
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
        """画图"""
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'
        plt.scatter(X_test, ypre)
        plt.plot(X_test, ypre, c='blue')
        plt.xlabel(u'小说字数')
        plt.ylabel(u'小说收藏数')
        plt.title(u"小说字数和收藏数关系模型")
        plt.savefig(name_png + '.png', dpi=600)
        plt.show()


if __name__ == '__main__':
    modelPredict = ModelPredict()
    modelPredict.get_train(modelPredict.data_man_txt, modelPredict.train_x_man, modelPredict.train_y_man)
    modelPredict.get_train(modelPredict.data_woman_txt, modelPredict.train_x_woman, modelPredict.train_y_woman)
    modelPredict.model_predict(modelPredict.train_x_man, modelPredict.train_y_man, 3, "man")
    modelPredict.model_predict(modelPredict.train_x_woman, modelPredict.train_y_woman, 2, "woman")
