'''综合应用'''


import pandas as pd

price_df = pd.DataFrame({
    "date":[
        "2023-01-01",
        "2023-01-01",
        "2023-01-02",
        "2023-01-03",
        "2023-01-01",
        "2023-01-02",
        "2023-01-03"
    ],

    "code":[
        "A","A","A","A",
        "B","B","B"
    ],

    "close":[
        10,10,11,12,
        20,19,21
    ]
})

factor_df = pd.DataFrame({
    "date":[
        "2023-01-01",
        "2023-01-02",
        "2023-01-03",
        "2023-01-01",
        "2023-01-02",
        "2023-01-03"
    ],

    "code":[
        "A","A","A",
        "B","B","B"
    ],

    "factor":[
        0.1,0.2,0.3,
        0.15,None,0.05
    ]
})

'''日期转换'''
price_df["date"] = pd.to_datetime(price_df["date"])
factor_df["date"] = pd.to_datetime(factor_df["date"])


'''去重'''
price_df = price_df.drop_duplicates(
    subset = ["date", "code"]
)

factor_df_df = factor_df.drop_duplicates(
    subset = ["date", "code"]
)

'''排序'''
price_df = price_df.sort_values(
    ["code", "date"]
)

'''计算收益率'''
price_df["return"] = price_df.groupby("code")["close"].pct_change()

'''昨日收盘'''
price_df["yesterday_close"] = price_df.groupby("code")["close"].shift(1)

'''2日均线'''
price_df["ma2"] = (
    price_df.groupby("code")["close"]
        .transform(
            lambda x: x.rolling(2).mean()
        )
)

'''未来一日收益'''
price_df["tommorrow_return"] = (
    price_df.groupby("code")["close"]
        .shift(-1)
    /price_df["close"]
    - 1
)

'''并表'''
result = pd.merge(
    price_df,
    factor_df,
    on = ["date", "code"],
    how = "left"
)

'''因子排名'''
result["rank"] = (
    result.groupby("date")["factor"]
        .rank(
            ascending = False,
            method = "min"
        )
)
print(result)
