# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn import preprocessing
import pywt
import pywt.data
import pandas as pd

data_file = 'Exp5_480Hz.csv'



def get_data():
    """
    获取数据
    Returns:

    """
    data = []
    df = pd.read_csv(data_file)
    df = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
    for index, row in df.iterrows():
        # print(row.values)
        data_row = row.to_numpy()
        for i in data_row:
            if i > 0:
                data.append(i)
    data = np.array(data)
    print(data)
    return data


def wpd_plt(signal, n):
    # wpd分解
    wp = pywt.WaveletPacket(data=signal, wavelet='db1', mode='symmetric', maxlevel=n)

    # 计算每一个节点的系数，存在map中，key为'aa'等，value为列表
    map = {}
    map[1] = signal
    for row in range(1, n + 1):
        lev = []
        for i in [node.path for node in wp.get_level(row, 'freq')]:
            map[i] = wp[i].data
    energy = []
    for k, v in map.items():
        for i in v:
            energy.append(pow(np.linalg.norm(i, ord=None), 2))
    E = np.sum(energy)

    print(energy)
    energy = [i for i in energy if(i!= 0)]
    print(len(energy))
    c28 = -np.sum((energy/E) * np.log10(energy/E))
    print("c28:", c28)

    # 作图
    plt.figure(figsize=(15, 10))
    plt.subplot(n + 1, 1, 1)  # 绘制第一个图
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.plot(map[1])
    for i in range(2, n + 2):
        level_num = pow(2, i - 1)  # 从第二行图开始，计算上一行图的2的幂次方
        # 获取每一层分解的node：比如第三层['aaa', 'aad', 'add', 'ada', 'dda', 'ddd', 'dad', 'daa']
        re = [node.path for node in wp.get_level(i - 1, 'freq')]
        for j in range(1, level_num + 1):
            plt.subplot(n + 1, level_num, level_num * (i - 1) + j)
            plt.plot(map[re[j - 1]])  # 列表从0开始
    plt.show()


if __name__ == '__main__':
    wpd_plt(get_data(), 5)