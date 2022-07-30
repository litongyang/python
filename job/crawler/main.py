# coding=utf-8
import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf8')
url = "https://www.bitpush.news/covid19/"
# 设置请求头信息
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}
# 使用reqeusts模快发起 GET 请求
response = requests.get(url, headers=headers)
# 获取请求的返回结果
html = response.text
parse = etree.HTMLParser(encoding='utf-8')
doc = etree.HTML(html)
# 州
state = doc.xpath('//div[@class="table_container"]//tbody/tr/td/span/text()')
# 确诊人数
person = doc.xpath('//div[@class="table_container"]//tbody/tr/td[2]/text()')
# 由于确诊人数中有逗号，我们使用列表推导式删除
person = [x.replace(",", "") for x in person]
# 死亡人数
death = doc.xpath('//div[@class="table_container"]//tbody/tr/td[3]/text()')
# 同样使用列表推导式删除逗号
death = [x.replace(",", "") for x in death]
#打包数据之后将其转换成列表
message = list(zip(state, person, death))
print message


with open("content.csv", "w", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerows(message)


df = pd.read_csv("content.csv", names=["state", "person", "death"])
print(df.head(102))
print(df.info())
for i in range(101):
    df = df.drop(index=i)
print(df.head())
df = df.head(15)


# 在jupyter中直接展示图像
#%matplotlib inline
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['figure.figsize'] = (10, 5)  # 设置figure_size尺寸

# x轴坐标
x = df["state"].values
# y轴坐标
y = df["person"].values
# 绘制柱状图
plt.bar(x, y)
# 设置x轴名称
plt.xlabel("州",fontsize=10)
# 设置x轴名称
plt.ylabel("确诊人数",fontsize=14)
plt.show()