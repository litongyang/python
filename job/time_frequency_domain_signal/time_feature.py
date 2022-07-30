# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_name = 'Exp5_480Hz.csv'

"""
计算时域频率特征
"""

def psfeature_time(p1, p2):
    """
    时域信号特征提取
    :param p1: 一次计算的起始点
    :param p2: 一次计算的终止点
    :return:featuretime_list
    """
    df = pd.read_csv(file_name)
    df = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
    data_list = []
    for index, row in df.iterrows():
        data = row.to_numpy()
        for i in data:
            data_list.append(i)
    data = np.array(data_list)
    print(data)

    # 均值
    df_mean = data[p1:p2].mean()
    df_var = data[p1:p2].var()
    df_std = data[p1:p2].std()
    # 均方根
    df_rms = np.sqrt(pow(df_mean, 2) + pow(df_std, 2))
    # 峰峰值
    fengfengzhi = max(data[p1:p2]) - min(data[p1:p2])

    sum = 0
    for p1 in range(len(data[p1:p2])):
        sum += np.sqrt(abs(data[p1]))

    # 波形因子
    df_boxing = df_rms / (abs(data[p1:p2]).mean())
    # 峰值因子
    df_fengzhi = (max(data[p1:p2])) / df_rms
    # 脉冲因子
    df_maichong = (max(data[p1:p2])) / (abs(data[p1:p2]).mean())
    # 裕度因子
    df_yudu = max(data[p1:p2]) / pow(sum / (p2 - p1), 2)
    # 峭度
    df_qiaodu = (np.sum([x ** 4 for x in data[p1:p2]]) / len(data[p1:p2])) / pow(df_rms, 4)
    featuretime_list = [round(df_rms, 3), round(fengfengzhi, 3), round(df_fengzhi, 3), round(df_boxing, 3),
                        round(df_maichong, 3), round(df_yudu, 3), round(df_qiaodu, 3)]
    return featuretime_list


if __name__ == '__main__':
    # 当前位置
    p1 = 1
    # 采样频率
    sampl_frequency = 100
    # 按照采样频率下一次到达的位置
    p2 = p1 + sampl_frequency

    # 统计该文件有多少行？
    total_lines = 192000
    print('The total lines is ', total_lines)

    times = int(total_lines / sampl_frequency)
    print ('The total times is ', times)

    divisor_list = []

    df_boxing_list = []
    df_fengzhi_list = []
    df_maichong_list = []
    df_yudu_list = []
    df_qiaodu_list = []
    df_rms_list = []

    for i in range(times):
        print ("第" + str(i+1) + "次")
        divisor_list = psfeature_time(i * sampl_frequency, i * sampl_frequency + sampl_frequency)
        print(divisor_list)
        df_boxing_list.append(float(divisor_list[3]))
        df_fengzhi_list.append(float(divisor_list[2]))
        df_maichong_list.append(float(divisor_list[4]))
        df_yudu_list.append(float(divisor_list[5]))
        df_qiaodu_list.append(float(divisor_list[6]))
        # df_rms_list.append(float(divisor_list[4]))
        print ("df_boxing_list", df_boxing_list)
    x = [i for i in range(1, len(df_boxing_list)+1)] # x轴
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'

    """波形因子画图"""
    plt.scatter(x, df_boxing_list)
    plt.plot(x, df_boxing_list)
    plt.title(u'波形因子')
    plt.xlabel(u'采样次数')
    plt.ylabel(u'波形因子')
    plt.savefig(u'波形因子')
    plt.show()

    """峰值因子画图"""
    plt.scatter(x, df_fengzhi_list)
    plt.plot(x, df_fengzhi_list)
    plt.title(u'峰值因子')
    plt.xlabel(u'采样次数')
    plt.ylabel(u'峰值因子')
    plt.savefig(u'峰值因子')
    plt.show()

    """脉冲因子画图"""
    plt.scatter(x, df_maichong_list)
    plt.plot(x, df_maichong_list)
    plt.title(u'脉冲因子')
    plt.xlabel(u'采样次数')
    plt.ylabel(u'脉冲因子')
    plt.savefig(u'脉冲因子')
    plt.show()

    """裕度因子画图"""
    plt.scatter(x, df_yudu_list)
    plt.plot(x, df_yudu_list)
    plt.title(u'裕度因子')
    plt.xlabel(u'采样次数')
    plt.ylabel(u'裕度因子')
    plt.savefig(u'裕度因子')
    plt.show()

    """峭度因子画图"""
    plt.scatter(x, df_qiaodu_list)
    plt.plot(x, df_qiaodu_list)
    plt.title(u'峭度因子')
    plt.xlabel(u'采样次数')
    plt.ylabel(u'峭度因子')
    plt.savefig(u'峭度因子')
    plt.show()


