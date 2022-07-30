# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
求频域特征
"""


class Feature:
    def __init__(self):
        self.data_file = 'Exp5_480Hz.csv'
        self.data = []
        self.Fs = 19000

    def get_data(self):
        """
        获取数据
        Returns:

        """
        df = pd.read_csv(self.data_file)
        df = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
        for index, row in df.iterrows():
            # print(row.values)
            data = row.to_numpy()
            for i in data:
                self.data.append(i)
        self.data = np.array(self.data)

    def get_feature(self,p1,p2):

        L = len(self.data[p1:p2])
        PL = abs(np.fft.fft(self.data[p1:p2] / L))[: int(L / 2)]
        PL[0] = 0
        f = np.fft.fftfreq(L, 1 / self.Fs)[: int(L / 2)]
        x = f
        y = PL
        K = len(y)
        print("self.data.shape:", self.data[p1:p2].shape)
        print("PL.shape:", PL.shape)
        print("L:", L)
        print("K:", K)
        print("x:",x)
        print("y:",y)
        c18 = np.max(y)
        c19 = np.min(y)
        c20 = np.median(y)
        c21 = np.mean(y)
        c22 = c18-c19
        c23 = np.sum(y*x)/np.sum(y)
        c24 = np.sqrt((np.sum((x**2)*y))/(np.sum(y)))
        c25 = (np.sum((x**2)*y))/(np.sum(y))
        c26 = np.sum(((x-c23)**2) *(x/np.sum(x)))
        c27 = np.sqrt(c26)
        # print((x-c23)**2)
        # print(x/np.sum(x))
        feature_list = [c18, c19, c20, c21, c22, c23, c24, c25, c26, c27]
        return feature_list


if __name__ == '__main__':
    feature = Feature()
    feature.get_data()
    # 当前位置
    p1 = 1
    # 采样频率
    sampl_frequency = 100
    # 按照采样频率下一次到达的位置
    p2 = p1 + sampl_frequency

    # 统计该文件有多少行？
    total_lines = len(feature.data)
    print('The total lines is ', total_lines)
    times = int(total_lines / sampl_frequency)
    print('The total times is ', times)
    c18_list = []
    c19_list = []
    c20_list = []
    c21_list = []
    c22_list = []
    c23_list = []
    c24_list = []
    c25_list = []
    c26_list = []
    c27_list = []

    for i in range(times):
        print ("第" + str(i+1) + "次")
        divisor_list = feature.get_feature(i * sampl_frequency, i * sampl_frequency + sampl_frequency)
        c18_list.append(divisor_list[0])
        c19_list.append(divisor_list[1])
        c20_list.append(divisor_list[2])
        c21_list.append(divisor_list[3])
        c22_list.append(divisor_list[4])
        c23_list.append(divisor_list[5])
        c24_list.append(divisor_list[6])
        c25_list.append(divisor_list[7])
        c26_list.append(divisor_list[8])
        c27_list.append(divisor_list[9])

    plt.plot(c18_list)
    plt.title('c18')
    plt.show()

    plt.plot(c19_list)
    plt.title('c19')
    plt.show()

    plt.plot(c20_list)
    plt.title('c20')
    plt.show()

    plt.plot(c21_list)
    plt.title('c21')
    plt.show()

    plt.plot(c22_list)
    plt.title('c22')
    plt.show()

    plt.plot(c23_list)
    plt.title('c23')
    plt.show()

    plt.plot(c24_list)
    plt.title('c24')
    plt.show()

    plt.plot(c25_list)
    plt.title('c25')
    plt.show()

    plt.plot(c26_list)
    plt.title('c26')
    plt.show()

    plt.plot(c27_list)
    plt.title('c27')
    plt.show()
