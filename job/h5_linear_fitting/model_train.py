# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import h5py
from pprint import pprint


class ModelTrain:
    def __init__(self):
        self.label_file = 'Le_interim.h5'
        self.train_file = '因子.xlsx'
        self.label = []  # 时间
        self.train_x = []  # p1、p2
        self.coef = []  # 模型训练参数
        self.intercept = []  # 模型训w0
        self.shift_orgin = 12
        self.shift_last = 384
        self.shift_min = -12
        self.shift_max = 12
        self.shift_data_dict_p1 = {}  # 所有位移数据的字典，key为位移单位，value为位移后的p1数据
        self.shift_data_dict_p2 = {}  # 所有位移数据的字典，key为位移单位，value为位移后的p2数据
        self.residual_dict = {}  # 残差字典

    def get_label_data(self):
        """
        获取label数据
        Returns:

        """
        with h5py.File(self.label_file, "r") as f:
            for key in f.keys():
                if key == 'Le':
                    for i in range(0, 11):
                        le1 = f[key].value[:, i, :]
                        for j in range(0, 174):
                            le2 = le1[:, j]
                            self.label.append(le2)

    def get_label(self):
        """
        得到label的平滑数据
        Returns:

        """


    def get_train_data(self):
        """
        获取p1、p2的训练数据
        Returns:

        """
        p1_pd = pd.read_excel(self.train_file, sheet_name='p1', header=None)
        p2_pd = pd.read_excel(self.train_file, sheet_name='p2', header=None)
        p1_data = np.array(p1_pd[0].values)
        p2_data = np.array(p2_pd[0].values)
        # t_list = list(range(1, 373))
        for i in range(0, len(p1_data)):
            # train_one = [t_list, p1_data[i], p2_data[i]]
            train_one = [i+1, p1_data[i], p2_data[i]]
            # train_one = [p1_data[i], p2_data[i]]
            self.train_x.append(train_one)

    def get_model(self):
        """
        模型训练，保存参数
        Returns:

        """
        for i in range(0, len(self.label)):
            lr = LinearRegression(fit_intercept=True)
            model = lr.fit(self.train_x, self.label[i])
            coef_one = model.coef_
            intercept_one = model.intercept_
            self.coef.append(coef_one)
            self.intercept.append(intercept_one)
        # print(self.coef)
        # x = np.reshape(self.coef,(11,174))
        # print(x)
        # temp = []
        # for i in range(0, len(self.coef)):
        #     two = []
        #     for j in range(i, 11):
        #         # print(self.coef[i+j])
        #         two.append(self.coef[j])
        #     i += 11
        #     temp.append(two)
        # print(temp)
        arr2 = []
        for index in range(0, len(self.coef), 174):
            arr2.append(self.coef[index:index + 174])
        np.save('test', np.array(arr2))

    def get_shift_data(self):
        """
        得到位移数据
        位移范围-12~12
        步长：1
        Returns:

        """
        p1_shift_array = []
        p2_shift_array = []
        """获取p1一维数组"""
        p1_shift_pd = pd.read_excel(self.train_file, sheet_name='p1_shift', header=None)
        for i in range(0, len(p1_shift_pd.values)):
            for j in range(0, len(p1_shift_pd.values[i])):
                p1_shift_array.append(p1_shift_pd.values[i][j])

        """获取p2一维数组"""
        p2_shift_pd = pd.read_excel(self.train_file, sheet_name='p2_shift', header=None)
        for i in range(0, len(p2_shift_pd.values)):
            for j in range(0, len(p2_shift_pd.values[i])):
                p2_shift_array.append(p2_shift_pd.values[i][j])
        for i in range(self.shift_min, self.shift_max+1):
            if i != 0:
                self.shift_data_dict_p1[str(i)] = p1_shift_array[self.shift_orgin+i: self.shift_last+i]
                self.shift_data_dict_p2[str(i)] = p2_shift_array[self.shift_orgin+i: self.shift_last+i]

    def compute_residual(self):
        """
        计算残差
        Returns:

        """
        y_pre = []
        for k, v in self.shift_data_dict_p1.items():
            y_pre_arr2 = []
            y_pre_2 = []
            model_residual = []
            for i in range(0, len(self.coef)):
                one_model_pre_v = []  # 一个模型的预测值
                for i in range(0, len(v)):
                    one_model_pre_v.append(self.coef[i][0] * i +self.coef[i][1] * v[i] + self.coef[i][2] * self.shift_data_dict_p2[k][i]
                                           + self.intercept[i])
                y_pre_2.append(one_model_pre_v)
                one_model_residual = np.sum(one_model_pre_v - self.label[i])
                # print(len(one_model_pre_v))
                model_residual.append(one_model_residual)
            self.residual_dict[k] = np.sum(model_residual)
            print(self.residual_dict)
            for index in range(0, len(y_pre_2), 174):
                y_pre_arr2.append(y_pre_2[index:index + 174])
            # print(np.array(y_pre_arr2).shape)
            y_pre.append(y_pre_arr2)
        print(np.array(y_pre).shape)
        np.save('y_pre', np.array(y_pre))

        min_value = min(self.residual_dict.values())
        for k, v in self.residual_dict.items():
            if v == min_value:
                print(k)


if __name__ == '__main__':
    model_train = ModelTrain()
    model_train.get_label_data()
    model_train.get_train_data()
    model_train.get_model()
    model_train.get_shift_data()
    model_train.compute_residual()



