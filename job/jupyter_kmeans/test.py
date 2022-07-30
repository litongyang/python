import pandas as pd
from sklearn.datasets import load_boston

import statsmodels.api as sm
import numpy as np

''' 数据demo'''
x = [1,2]
y = [1,4]
two_arr = [[1,2,3],[4,5,6]]
one_arr = sum(two_arr,[])
print(one_arr)
import scipy.stats as stats
t, p = stats.ttest_ind(x,y)
print(p)
