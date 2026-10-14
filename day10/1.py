'''正态分布和Z-score

    Z(x) = (x - x.mean()) / x.std()
'''

import pandas as pd

df = pd.DataFrame({
    "date": [
        "2023-01-01",
        "2023-01-01",
        "2023-01-01",
        "2023-01-02",
        "2023-01-02",
        "2023-01-02"
    ],
    "code": ["A", "B", "C", "A", "B", "C"],
    "factor": [10, 20, 30, 15, 25, 35]
})

df["factor_z"] = (
    df.groupby("date")["factor"]
        .transform(
            lambda x : (x - x.mean()) / x.std()
        )
)

print(df)

print(df.groupby("date")["factor_z"].mean())