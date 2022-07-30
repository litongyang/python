
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV

data_file = '融指数据.xlsx'


class ModelTrain:
    """
    模型训练
    """

    def __init__(self):
        self.df_out = pd.read_excel(data_file)
        self.df_in = pd.read_excel(data_file, sheet_name='操作变量')
        self.train_one_x = []
        self.train_one_y = []
        self.train_x = []
        self.train_y = []

    def get_data(self):
        """

        Returns:

        """
        data_pd = pd.merge(self.df_out, self.df_in, on='TEMP')
        data_pd = pd.DataFrame(data_pd, columns=['样品名称', '显示值', 'TEMP', 'Tem', 'Pre', 'TICL4', 'TEAL', 'donor', 'C3H6',
                                                 'R201tem', 'Pre.1', 'R201h2/c3h6', 'R202tem', 'Pre.2', 'R202h2/c3h6'])
        """选出一种商品"""
        data_one_pd = data_pd[data_pd['样品名称'] == '干燥器D502底部出口粉料PPH-Y26']
        self.train_one_x = pd.DataFrame(data_one_pd, columns=['Tem', 'Pre', 'TICL4', 'TEAL', 'donor', 'C3H6',
                                                      'R201tem', 'Pre.1', 'R201h2/c3h6', 'R202tem', 'Pre.2',
                                                      'R202h2/c3h6'])
        self.train_one_y = pd.DataFrame(data_one_pd, columns=['显示值'])

        """全品种"""
        self.train_x = pd.DataFrame(data_pd, columns=['Tem', 'Pre', 'TICL4', 'TEAL', 'donor', 'C3H6',
                                                      'R201tem', 'Pre.1', 'R201h2/c3h6', 'R202tem', 'Pre.2',
                                                      'R202h2/c3h6'])
        self.train_y = pd.DataFrame(data_pd, columns=['显示值'])
        """数据分析"""
        gl_group_mean = data_pd.groupby("样品名称").mean()
        gl_group_median = data_pd.groupby("样品名称").median()
        gl_group_max = data_pd.groupby("样品名称").max()
        gl_group_min = data_pd.groupby("样品名称").min()
        gl_group_mean.to_excel("mean.xlsx")
        gl_group_median.to_excel("median.xlsx")
        gl_group_max.to_excel("max.xlsx")
        gl_group_min.to_excel("min.xlsx")

        """数据处理"""
        imp_median = SimpleImputer(strategy="median")
        imp_median.fit_transform(self.train_x.values.reshape(1, -1))

        """数据分析"""
        line = PCA().fit(self.train_x)
        print(line.explained_variance_ratio_)
        plt.plot(range(1, 13), line.explained_variance_ratio_)
        plt.xticks(range(1,13))  # 横坐标轴显示的整数坐标
        plt.xlabel('label_num')
        plt.ylabel('Contribution rate')
        plt.title('feature Contribution rate')
        plt.show()
        # 特征工程
        scaler = MinMaxScaler()  # 实例化
        scaler = scaler.fit(self.train_x)  # fit，在这里本质是生成min(x)和max(x)
        self.train_x = scaler.transform(self.train_x)
        """升维"""
        self.train_x = np.hstack([self.train_x, self.train_x])
        print(self.train_x.shape)

    def model_train_one(self):
        """
        训练单一品种模型
        Returns:

        """
        X_train, X_test, Y_train, Y_test = train_test_split(self.train_one_x, self.train_one_y, test_size=0.3, random_state=0)
        clf = GradientBoostingRegressor(learning_rate=0.1, n_estimators=60, min_samples_leaf=20,
                                        max_features='sqrt', subsample=0.8, random_state=10,
                                        max_depth=3, min_samples_split=100)
        model = clf.fit(X_train, Y_train)
        y_pre = model.predict(X_test)
        """评估模型"""
        print("平均绝对误差:", mean_absolute_error(Y_test, y_pre))  # 平均绝对误差
        print("方差得分:", explained_variance_score(Y_test, y_pre))  # 方差得分
        print("均方差:", mean_squared_error(Y_test, y_pre))  # 均方差
        print("判定系数", r2_score(Y_test, y_pre))  # 判定系数

    def model_train(self):
        """
        训练全品种模型
        Returns:

        """
        X_train, X_test, Y_train, Y_test = train_test_split(self.train_x, self.train_y, test_size=0.3, random_state=0)
        """模型调参"""
        param_test2 = {'max_depth': range(3, 20, 2), 'min_samples_split': range(100, 801, 200)}
        gsearch2 = GridSearchCV(
            estimator=GradientBoostingRegressor(learning_rate=0.1, n_estimators=60, min_samples_leaf=20,
                                                 max_features='sqrt', subsample=0.8, random_state=10),
            param_grid=param_test2, scoring='roc_auc', cv=5)
        gsearch2.fit(X_train, Y_train)
        print( gsearch2.best_params_, gsearch2.best_score_)

        """构建模型"""
        clf = GradientBoostingRegressor(learning_rate=0.1, n_estimators=60, min_samples_leaf=20,
                                        max_features='sqrt', subsample=0.8, random_state=10,
                                        max_depth=3, min_samples_split=100)
        model = clf.fit(X_train, Y_train)
        y_pre = model.predict(X_test)
        # # print(y_pre)

        """评估模型"""
        print("平均绝对误差:", mean_absolute_error(Y_test, y_pre))  # 平均绝对误差
        print("方差得分:", explained_variance_score(Y_test, y_pre))  # 方差得分
        print("均方差:", mean_squared_error(Y_test, y_pre))  # 均方差
        print("判定系数", r2_score(Y_test, y_pre))  # 判定系数


if __name__ == '__main__':
    model_train = ModelTrain()
    model_train.get_data()
    model_train.model_train_one()
    model_train.model_train()
