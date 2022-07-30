# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import sys

lease_cnt = pd.read_excel(u'测试.xls', sheet_name="Sheet1", encoding='utf-8')[u'在租数量'].values
sale_cnt = pd.read_excel(u'测试.xls', sheet_name="Sheet1", encoding='utf-8')[u'在售数量'].values
lease_s_min = pd.read_excel(u'测试.xls', sheet_name="Sheet1", encoding='utf-8')[u'在租短租最低价'].values
sale_s_min = pd.read_excel(u'测试.xls', sheet_name="Sheet1", encoding='utf-8')[u'在租长租最低价'].values
sale_min = pd.read_excel(u'测试.xls', sheet_name="Sheet1", encoding='utf-8')[u'在售最低价'].values
saled_cnt = pd.read_excel(u'测试.xls', sheet_name="Sheet1", encoding='utf-8')[u'历史成交数量']
print lease_cnt

list_x = []
list_y = []


def compute_0(list):
    cnt_0 = 0
    cnt_1 = 0
    for i in list:
        if i == 0:
            cnt_0 += 1
        else:
            cnt_1 += 1
    return cnt_0, cnt_1


x1, y1 = compute_0(lease_cnt)
x2, y2 = compute_0(sale_cnt)
x3, y3 = compute_0((np.array(saled_cnt)-1).tolist())
list_x.append(x1)
list_x.append(x2)
list_x.append(x3)
list_y.append(y1)
list_y.append(y2)
list_y.append(y3)
x= [u'在租', u'在售', u'成交']


plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
plt.style.use('ggplot')  # 设置ggplot样式

plt.bar(x, list_x, label=u'没有交易数量')
plt.bar(x, list_y, label=u'交易数量')
plt.xlabel('years')
plt.ylabel(u'没有交易数量/交易数量')
plt.title(u'网站商品交易与没有交易量的对比')
plt.legend()
plt.show()


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'
plt.pie(list_x, labels=x, autopct='%3.1f%%')
plt.title(u"网站商品交易与没有交易量的对比")
plt.show()

