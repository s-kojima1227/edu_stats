import numpy as np

# 指数分布の分布関数の逆関数 (分位関数)
class ExpQuantile:
    def __init__(self, lam):
        self._lam = lam

    def __call__(self, p):
        return -np.log(1 - p) / self._lam

# 逆変換法
class InverseTransformationMethod:
    def __init__(self, quantile):
        self._quantile = quantile

    def __call__(self):
        # 一様乱数を生成
        u = np.random.rand()
        # 分位関数の値を計算
        x = self._quantile(u)
        return x
