# -*- coding: utf-8 -*-

import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
import collections
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import multilabel_confusion_matrix
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt


class ModelTrain:
    """
    训练mnist数据
    """

    @staticmethod
    def load_mnist(path, kind='train'):
        """
        获取训练集和测试剂数据
        """
        labels_path = path + '%s-labels.idx1-ubyte' % kind
        images_path = path + '%s-images.idx3-ubyte' % kind

        with open(labels_path, 'rb') as lbpath:
            labels = np.frombuffer(lbpath.read(), dtype=np.uint8, offset=8)
        with open(images_path, 'rb') as imgpath:
            images = np.frombuffer(imgpath.read(), dtype=np.uint8, offset=16).reshape(len(labels), 784)
        return images, labels

    @staticmethod
    def data_cleaning_analysis(images, labels):
        """对于空值的处理"""
        print(images.shape)
        sim = SimpleImputer(missing_values=np.nan, strategy='mean')
        images = sim.fit_transform(images)

        """数据分析"""
        # 调用PCA,降维训练
        # pca = PCA(n_components=1)  # 实例化
        # pca_train = pca.fit(images)  # 拟合模型
        # X_tran_dr = pca_train.transform(images)  # 获取新矩阵
        # X_train_dr = X_tran_dr.tolist()
        # x_train_pca=[]
        # for i in range(0, len(X_train_dr)):
        #     x_train_pca.append(X_train_dr[i][0])
        # print(x_train_pca)
        # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        # plt.scatter(range(len(x_train_pca)), x_train_pca)
        # plt.title(u'pca降维后训练集的散点图分布')
        # plt.show()

        """训练集label分布情况"""
        # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        # cnt = collections.Counter(labels)
        # print(cnt)
        # for k, v in cnt.items():
        #     plt.bar(k, v,color='blue')
        # plt.title(u'训练集label分布情况')
        # plt.show()

        """特征选择"""
        print(images.shape)
        X_fschi = SelectKBest(chi2, k=300).fit_transform(images, labels)
        print(X_fschi.shape)

        """数据标准化：# Z-score标准化"""
        ss = StandardScaler()
        images = ss.fit_transform(images)
        print(images)

    @staticmethod
    def model_randomForest(x_train, y_train, x_test, y_test):
        """
        随机森林模型训练
        """
        clf = RandomForestClassifier(bootstrap=True, oob_score=True, criterion='gini', n_estimators=90)
        model = clf.fit(x_train, y_train)  # 训练
        y_pre = model.predict(x_test)
        report = classification_report(y_test, y_pre)
        """200次交叉验证，得到最合适的n_estimators"""
        # superpa = []
        # for i in range(200):
        #     rfc = RandomForestClassifier(n_estimators=i + 1, n_jobs=-1)
        #     rfc_s = cross_val_score(rfc, x_train, y_train, cv=10).mean()
        #     superpa.append(rfc_s)
        # plt.figure()
        # plt.plot(range(1, 201), superpa)
        # plt.savefig('n_estimators_best')
        # plt.show()
        print('......................打印随机森林模型评估报告................')
        print(report)
        mcm = multilabel_confusion_matrix(y_test, clf.predict(X_test))  # mcm即为混淆矩阵
        print('......................打印混淆矩阵................')
        print(mcm)

    @staticmethod
    def model_decisionTree(x_train, y_train, x_test, y_test):
        """
        决策树模型训练
        """
        clf = DecisionTreeClassifier(random_state=25, criterion="entropy", max_depth=10)
        model = clf.fit(x_train, y_train)  # 训练
        y_pre = model.predict(x_test)
        report = classification_report(y_test, y_pre)
        """求最佳树深度"""
        # tr = []
        # te = []
        # for i in range(7, 15):
        #     clf = DecisionTreeClassifier(random_state=25
        #                                  , max_depth=i + 1
        #                                  , criterion="entropy"
        #                                  )
        #     clf = clf.fit(x_train, y_train)
        #     score_tr = clf.score(x_train, y_train)
        #     score_te = cross_val_score(clf, x_train, y_train, cv=10).mean()  # 交叉验证取均值作测试
        #     tr.append(score_tr)
        #     te.append(score_te)
        # print(max(te))
        # plt.plot(range(1, 9), tr, color="red", label="train")
        # plt.plot(range(1, 9), te, color="blue", label="test")
        # plt.xticks(range(1, 9))  # 限制x轴显示范围
        # plt.legend()  # 显示图例
        # plt.savefig('decisionTree')
        # plt.show()

        print('......................打印决策树模型评估报告................')
        print(report)
        mcm = multilabel_confusion_matrix(y_test, clf.predict(X_test))  # mcm即为混淆矩阵
        print('......................打印混淆矩阵................')
        print(mcm)


if __name__ == '__main__':
    model_train = ModelTrain()
    X_train, y_train = model_train.load_mnist('.\\', kind='train')
    X_test, y_test = model_train.load_mnist('.\\', kind='t10k')
    # model_train.data_cleaning_analysis(X_train, y_train)
    # model_train.model_randomForest(X_train, y_train, X_test, y_test)
    model_train.model_decisionTree(X_train, y_train, X_test, y_test)