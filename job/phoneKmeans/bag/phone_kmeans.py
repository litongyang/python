# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples


class PhoneKmeans:
    def __init__(self):
        self.name_bag_w_txt = "20-bag-w.txt"
        self.name_bag_y_txt = "20-bag-y.txt"
        self.name_bag_yin_txt = "20-bag-yin.txt"
        self.bag_w = []
        self.bag_y = []
        self.bag_yin = []
        self.bag_train = []


    @staticmethod
    def data_cleaning(file_name, data_list, train_list):
        """
       数据清洗，获取训练集
       :return:
       """
        for line in open(file_name):
            if line == '\n':
                continue
            line_list = line.split(' ')
            if len(line_list) == 4 :
                line_list = line_list[0:len(line_list)-1]
                line_list = [float(num) for num in line_list]
                train_list.append(line_list)
                data_list.append(line_list)

    @staticmethod
    def amplitude_drawing(data_list, name):
        """
        振幅画图
        :return:
        """
        x_axis = []
        y_axis = []
        z_axis = []
        A = []
        for dot in data_list:
            x_axis.append(dot[0])
            y_axis.append(dot[1])
            z_axis.append(dot[2])
            A.append(math.sqrt(dot[0]*dot[0] + dot[1]*dot[1] + dot[2]*dot[2]))
        plt.plot(x_axis, c='red')
        plt.plot(y_axis, c='green')
        plt.plot(z_axis, c='blue')
        plt.plot(A, c='black')
        title = "Amplitude 0f " + str(name) + " in 20HZ(black:Amplitude,blue:z_axis,green:y_axis,red:x_axis)"
        plt.title(title)
        plt.savefig(name+'.png', dpi=600)
        plt.show()

    def kmeans(self):
        """
        聚类
        :return:
        """
        model = KMeans(n_clusters=3, init='random')
        y_pred = model.fit_predict(self.bag_train)
        centers = model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], model.cluster_centers_[:, 2]
        print ("中心点坐标：",centers)
        # inertia和轮廓系数的对比
        inertia_scores = []
        sil_scores = []
        for n in range(2, 10):
            km = KMeans(n_clusters=n).fit(self.bag_train, y_pred)

            inertia_scores.append(km.inertia_)

            # 轮廓系数接收的参数中，第二个参数至少有两个分类
            sc = silhouette_score(self.bag_train, km.labels_)
            sil_scores.append(sc)
            print("n_clusters: {}\tinertia: {}\tsilhoutte_score: {}".format(
                n, km.inertia_, sc))


if __name__ == '__main__':
    phoneKmeans = PhoneKmeans()
    phoneKmeans.data_cleaning(phoneKmeans.name_bag_w_txt, phoneKmeans.bag_w, phoneKmeans.bag_train)
    phoneKmeans.data_cleaning(phoneKmeans.name_bag_y_txt, phoneKmeans.bag_y, phoneKmeans.bag_train)
    phoneKmeans.data_cleaning(phoneKmeans.name_bag_yin_txt, phoneKmeans.bag_yin, phoneKmeans.bag_train)
    phoneKmeans.amplitude_drawing(phoneKmeans.bag_w, "wang")
    phoneKmeans.amplitude_drawing(phoneKmeans.bag_y, "yang")
    phoneKmeans.amplitude_drawing(phoneKmeans.bag_yin, "yin")
    phoneKmeans.kmeans()
