# -*- coding: utf-8 -*-
"""
生成九九乘法表
"""

with open('exercise7_1.txt','w') as f:
    for j in range(1,10):
        for i in range(1,j+1):
            f.write(str(i)+'*'+str(j)+ '=' + str(i*j) + '\t')
        f.write('\n')

