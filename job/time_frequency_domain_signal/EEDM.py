# -*- coding: utf-8 -*-
import numpy as np
from PyEMD import EEMD, EMD, Visualisation
import matplotlib.pyplot as plt
import pandas as pd
import math

file_name = 'Exp5_480Hz.csv'


def Signal():
    max_imf = -1

    """
    信号参数：
    N:采样频率500Hz
    tMin:采样开始时间
    tMax:采样结束时间 2*np.pi
    """
    df = pd.read_csv(file_name)
    df = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
    data_list = []
    for index, row in df.iterrows():
        # print(row.values)
        data = row.to_numpy()
        for i in data:
            data_list.append(i)
    data = np.array(data_list)

    N = 480
    tMin, tMax = 0, 2 * np.pi
    T = np.linspace(tMin, tMax, N)  # 测试数据
    # T = data  # csv数据，运行时间过长
    print(T.shape)
    # 信号S:是多个信号叠加信号
    S = 3 * np.sin(4 * T) + 4 * np.cos(9 * T) + np.sin(8.11 * T + 1.2)

    # EEMD计算
    eemd = EEMD()
    eemd.trials = 50
    eemd.noise_seed(12345)
    E_IMFs = eemd.eemd(S, T, max_imf)
    # print(E_IMFs)
    imfNo = E_IMFs.shape[0]

    """计算能量熵"""
    for e in E_IMFs:
        E = np.sum(e)
        list_tmp =[]
        for ei in e:
            p = ei / E
            if math.isnan(p * np.log(p)):
                continue
            else:
                list_tmp.append(p * np.log(p))
        HEN = - sum(list_tmp)
        print("能量熵：", HEN)
        print("===============+++++++++++++++++++++++")

    # Plot results in a grid
    c = np.floor(np.sqrt(imfNo + 1))
    r = np.ceil((imfNo + 1) / c)
    plt.subplot(int(r), int(c), 1)
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.plot(T, S, 'r')
    # plt.xlim((tMin, tMax))
    plt.title("Original signal")

    for num in range(imfNo):
        plt.subplot(r, c, num + 2)
        plt.plot(T, E_IMFs[num], 'b')
        # plt.xlim((tMin, tMax))
        plt.title("Image " + str(num + 1))

    plt.show()


if __name__ == "__main__":
    Signal()
