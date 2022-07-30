# coding=utf-8
"""
画随机散点随机颜色图
"""
import matplotlib.pyplot as plt
import random
import numpy as np

data = np.array([4.29488806, -5.34487081])
x = random.sample(range(0, 50), 10)
y = random.sample(range(0, 50), 10)

c = [random.randint(0, 10) for _ in range(len(x))]
colors = ["b" if c > 5 else "r" for c in c]  # 随机颜色
print "x轴值：", x
print "y轴值：", y
print "颜色随机值：", colors
plt.scatter(x, y, s=200, alpha=0.5, c=colors, marker="o")
plt.show()
