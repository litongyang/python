# -*- coding: utf-8 -*-
import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.decomposition import PCA
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

class Classification:
    def __init__(self):
        self.X_train = []
        self.Y_train = []
        self.X_test= []
        self.Y_test = []

    def get_train_data(self, words, X, Y):
        """
        获取到训练和预测数据
        :return:
        """
        file_name_list = os.listdir('data\\%s' % words)
        file_name_data_dict = {}  # 构造文件名和数据的字典
        file_name_label_dict = {}  # 构造文件名和laibel的字典
        # file_name = 'data\\train\\' + str(file_name_list[0])
        for i in range(0, len(file_name_list)):
            file_name = 'data\\%s\\' % words + str(file_name_list[i])
            if str(file_name_list[i]) != '%s_label.dat' % words:
                data_pd = pd.read_csv(file_name, header=None, delimiter="\n")
                file_name_data_dict[file_name_list[i]] = data_pd
            else:
                data_pd = pd.read_csv(file_name, header=None, delimiter="\t")
                for row in data_pd.iterrows():
                    file_name_label_dict[row[1].values[0]] = row[1].values[1]
        for k, v in file_name_data_dict.items():
            for k1, v1 in file_name_label_dict.items():
                if k == k1:
                    one_train = []  # 存入一个文件的训练集数据
                    # print "v.values:",v.values
                    for i in range(0, len(v.values)):
                        one = v.values[i][0].split(',')
                        one = [int(num) for num in one]
                        one_train.append(one)
                    # print "one_train:", one_train
                    # 调用PCA
                    pca = PCA(n_components=1)  # 实例化
                    pca = pca.fit(one_train)  # 拟合模型
                    x_dr = pca.transform(one_train)  # 获取新矩阵
                    x_dr = x_dr.tolist()
                    x_test = []
                    for i in range(0, len(x_dr)):
                        x_test.append(x_dr[i][0])
                    # print "x_testlen:", len(x_test)
                    X.append(x_test)
                    Y.append(v1)
                    break
                    # self.X_train.append(v.values)
                    # self.Y_train.append(v1)
                    # print v.values
                    # print v1
                    # print "================"
        # for k, v in file_name_label_dict.items():
        #     print k,v

    def train_model(self):
        # -----训练模型--------------------
        # clf = LogisticRegression(random_state=0)
        # clf = tree.DecisionTreeClassifier(max_depth=10)
        # clf = svm.SVC(kernel='linear')
        clf = RandomForestClassifier(n_estimators=70, random_state=1, max_depth=80)
        model = clf.fit(self.X_train, self.Y_train)
        print'准确率:', model.score(self.X_test, self.Y_test)
        print'召回率:', recall_score(self.Y_test, model.predict(self.X_test))
        superpa = []
        """200次交叉验证，得到最合适的n_estimators"""
        for i in range(200):
            rfc = RandomForestClassifier(n_estimators=i + 1, n_jobs=-1)
            rfc_s = cross_val_score(rfc, self.X_train, self.Y_train, cv=10).mean()
            superpa.append(rfc_s)
        plt.figure()
        plt.plot(range(1, 201), superpa)
        plt.show()
        # print('精确率:', accuracy_score(y_test, l.predict(x_test)))
        # print('f1-score:', f1_score(y_test, l.predict(x_test)))



if __name__ == '__main__':
    classiftion = Classification()
    classiftion.get_train_data(words='train', X=classiftion.X_train, Y=classiftion.Y_train)
    classiftion.get_train_data(words='test', X=classiftion.X_test, Y=classiftion.Y_test)
    classiftion.train_model()
    # print classiftion.X_train
    # print classiftion.Y_train
    # print len(classiftion.X_test)
    # print len(classiftion.Y_test)
