import pandas as pd

df = pd.DataFrame({
    "date":["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-01", "2023-01-02", "2023-01-03"],
    "code":["A", "A", "A", "B", "B", "B"],
    "close":[10,11,12,20,18,21]
})

df["return"] = (
    df.groupby("code")["close"].pct_change()
)

df["ma2"] = (
    df.groupby("code")["close"]
    .transform(lambda x: x.rolling(2).mean())
)

print(df)
