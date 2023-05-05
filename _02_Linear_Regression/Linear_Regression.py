# 最终在main函数中传入一个维度为6的numpy数组，输出预测值

import os

try:
    import numpy as np
except ImportError as e:
    os.system("sudo pip3 install numpy")
    import numpy as np

def ridge(data):
    X,y = read_data()
    
    # 将 X 展平成二维数组
    n_samples = X.shape[0]
    X_flat = X.reshape((n_samples, -1))

    # 设置岭回归的超参数 alpha
    alpha = -0.1

    # 计算 X_flat 的转置矩阵
    X_flat_transpose = np.transpose(X_flat)

    # 计算矩阵 X_flat_transpose * X_flat + alpha * I 的逆矩阵
    inverse = np.linalg.inv(X_flat_transpose.dot(X_flat) + alpha * np.identity(X_flat.shape[1]))

    # 计算最优权重
    w = inverse.dot(X_flat_transpose).dot(y)
    return w @ data
   
def lasso(data):
    X, y = read_data()

    # 将 X 展平成二维数组
    n_samples = X.shape[0]
    X_flat = X.reshape((n_samples, -1))

    # 设置 Lasso 回归的超参数 alpha
    alpha = 0.1

    # 创建 Lasso 回归模型
    lasso = Lasso(alpha=alpha)

    # 训练模型
    lasso.fit(X_flat, y)
    return lasso.coef_ @ data

def read_data(path='./data/exp02/'):
    x = np.load(path + 'X_train.npy')
    y = np.load(path + 'y_train.npy')
    return x, y
