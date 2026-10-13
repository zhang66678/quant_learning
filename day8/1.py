"""均值、方差、标准差
    df["xxx"].mean()
    .var()
    .std()  默认ddof=1(即样本标准差, 分母是n-1) 总体标准差ddof=0
"""
import pandas as pd
import math

returns = pd.Series([
    0.01,
    0.02,
    -0.01,
    0.03,
    0.00
])

mean_returns = returns.mean()

variance = returns.var()

std = returns.std()

annual_volatility = std * math.sqrt(252)

print(mean_returns, variance, std, annual_volatility)