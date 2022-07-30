# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math
from sklearn.cluster import KMeans


class PhoneKmeans:
    def __init__(self):
        self.name_in_w_txt = "20-in-w.txt"
        self.name_in_y_txt = "20-in-y.txt"
        self.name_in_yin_txt = "20-in-yin.txt"
        self.in_w = []
        self.in_y = []
        self.in_yin = []
        self.in_train = []


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
        y_pred = model.fit_predict(self.in_train)
        centers = model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], model.cluster_centers_[:, 2]
        print ("中心点坐标：",centers)





if __name__ == '__main__':
    phoneKmeans = PhoneKmeans()
    phoneKmeans.data_cleaning(phoneKmeans.name_in_w_txt, phoneKmeans.in_w, phoneKmeans.in_train)
    phoneKmeans.data_cleaning(phoneKmeans.name_in_y_txt, phoneKmeans.in_y, phoneKmeans.in_train)
    phoneKmeans.data_cleaning(phoneKmeans.name_in_yin_txt, phoneKmeans.in_yin, phoneKmeans.in_train)
    phoneKmeans.amplitude_drawing(phoneKmeans.in_w, "wang")
    phoneKmeans.amplitude_drawing(phoneKmeans.in_y, "yang")
    phoneKmeans.amplitude_drawing(phoneKmeans.in_yin, "yin")
    phoneKmeans.kmeans()
