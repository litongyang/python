# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as ax


class PandasTest:
    """......读取数据集......"""
    def __init__(self):
        self.dataSet_1 = pd.read_excel('data_set.xls', sheet_name="Sheet1", encoding='utf-8')
        self.dataSet_2 = pd.read_excel('data_set.xls', sheet_name="Sheet2", encoding='utf-8')
        self.data_set = ''
        self.year = ''
        self.gdp = ''
        self.population = ''
        self.finance = ''
        self.gdp_avg = ''  # gdp均值
        self.gdp_var = ''  # gdp方差
        self.finance_avg = ''  # 财政收入均值
        self.finance_var= ''  # 财政收入方差


    """......数据清洗......"""
    def data_cleaning(self):
        self.data_set = pd.merge(self.dataSet_1, self.dataSet_2, how='outer')  # 数据集合并
        self.data_set.drop_duplicates()  # 数据去重
        self.data_set = self.data_set.fillna(value=None, method='ffill', axis=0, limit=None)  # 列向前填充空值
        self.data_set = self.data_set.fillna(value=None, method='bfill', axis=0, limit=None)  # 列向后填充空值


    """......数据抽取&数据选择&查看......"""
    def data_extract(self):
        self.year = self.data_set['year']  # 年份
        self.gdp = self.data_set['GDP(hundred million)']  # gdp
        self.population = self.data_set['population(ten thousand)']  #人口
        self.finance = self.data_set['finance(hundred million)']  # 财政
        print "查看数据索引\n",self.data_set.index
        print "查看列名\n",self.data_set.columns
        print "查看数据\n",self.data_set.values
        print "年份\n",self.year
        print "gdp历年数据\n",self.gdp
        print "人口历年数据\n",self.population
        print "财政收入历年数据\n",self.finance


    """......数据计算&数据排序......"""
    def compute_sort(self):
        self.gdp_avg = np.mean(self.gdp.values)  # gdp均值
        self.gdp_var = np.var(self.gdp.values)  # gdp方差
        self.finance_avg = np.mean(self.finance.values)  # 财政收入均值
        self.finance_var = np.var(self.finance.values)  # 财政收入方差

        print "gdp从小到大排序:\n",self.data_set.sort_values('GDP(hundred million)')  # gdp从小到大排序
        print "人口数量从小到大排序:\n",self.data_set.sort_values('population(ten thousand)')  # 人口数量从小到大排序


    """......画图......"""
    def drawing(self):
        # gdp每年增长的线状图
        plt.plot(self.year.values, self.gdp.values)
        plt.xlabel('years')
        plt.ylabel('GDP(hundred million)')
        plt.title('GDP growth curve')
        plt.savefig('gdp.png', dpi=400)
        plt.show()

        # gdp每年增长的点状图
        plt.scatter(self.year.values, self.gdp.values, s=200, alpha=0.5)
        plt.xlabel('years')
        plt.ylabel('GDP(hundred million)')
        plt.title('GDP growth curve')
        plt.savefig('gdp_scatter.png', dpi=400)
        plt.show()

        # 历年财政收入柱状图
        plt.bar(self.year.values, self.finance.values, color='#87CEFA')
        plt.xlabel('years')
        plt.ylabel('population(ten thousand)')
        plt.title('Finance growth curve')
        plt.savefig('finance.png', dpi=400)
        plt.show()

        # 历年财政收入和GDP占比
        plt.bar(self.year.values, self.gdp.values, label='gdp')
        plt.bar(self.year.values, self.finance.values, label='finance')
        plt.xlabel('years')
        plt.ylabel('GDP/finance')
        plt.title('GDP&finance contrast')
        plt.legend()
        plt.savefig('GDP&finance.png', dpi=400)
        plt.show()

        # 历年GDP、财政收入数据图
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.year, self.gdp.values, self.finance.values, c='r')
        ax.set_xlabel('years')
        ax.set_ylabel('GDP(hundred million)')
        ax.set_zlabel('finance(hundred million)')
        plt.title("yearss-GDP-finance")
        plt.savefig('year-GDP-finance3D', dpi=400)
        plt.show()




if __name__ == '__main__':
    padnasTest = PandasTest()
    padnasTest.data_cleaning()
    padnasTest.data_extract()
    padnasTest.compute_sort()
    padnasTest.drawing()

