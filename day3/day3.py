import pandas as pd

df = pd.DataFrame({
    "close":[100, 105, 103, 108, 110, 107]
})

df["ma2"] = df["close"].rolling(2).mean()

df["return"] = df["close"].pct_change()

df["volatility_3"] = df["return"].rolling(3).std()

print(df)