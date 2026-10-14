'''协方差、相关系数

    协方差 df["A"].cov(df["B"])
    相关系数 df["A"].corr(df["B"])  df.corr() 可以得到一个矩阵

'''

import pandas as pd

df = pd.DataFrame({
    "A": [0.01, 0.02, -0.01, 0.03, -0.02],
    "B": [0.008, 0.015, -0.005, 0.025, -0.015]
})

A = pd.Series([
    0.01,
    0.02,
    -0.01,
    0.03,
    -0.02
])

B = pd.Series([
    0.008,
    0.015,
    -0.005,
    0.025,
    -0.015
])

cov_AB = A.cov(B)
corr_AB = A.corr(B)

print(df.corr())

