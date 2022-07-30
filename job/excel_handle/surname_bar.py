# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import sys
reload(sys)
sys.setdefaultencoding('utf8')
"""
获取姓氏计数画柱状图
"""

names = pd.read_excel(u'21电气6班花名册.xls',sheet_name="Sheet1", encoding='utf-8')['姓名']
surname_list = []
#  获取姓氏
for name in names:
    surname_list.append(name[0])
# 构造姓氏计数字典
surname_cnt_dict = Counter(surname_list)
# 获取x、y轴的值
surname_x = []
surname_y = []
for k, v in surname_cnt_dict.items():
    surname_x.append(k)
    surname_y.append(v)
""" 调整姓氏顺序， 8是张，放在最前面 """
temp = surname_x[8]
surname_x[8] = surname_x[0]
surname_x[0] = temp

for i in range(0, len(surname_x)) :
    print i
    print surname_x[i]
# 画柱状图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'
plt.bar(surname_x, surname_y, color='#87CEFA')
plt.show()


