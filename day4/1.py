import pandas as pd

df = pd.DataFrame({
    "code":["A", "A", "A", "B", "B", "B"],
    "close":[10,11,12,20,18,21]
})

df["return"] = (
    df.groupby("code")["close"].pct_change()
)
df["yesterday_close"] = (
    df.groupby("code")["close"].shift(1)
)

print(df)