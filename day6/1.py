'''缺失值、重复值与基础数据清洗

    isna() 判断缺失值
    df["factor"].isna().sum() 统计缺失值数量
    print(df.isna().sum()) 打印每一列缺失值

    dropna() 删除缺失值
    df.dropna() 删除所有缺失值所在的行

    fillna() 填充缺失值
    df["factor"] = df["factor"].fillna(0) 将缺失值填充为0
    ffill() 前向填充
    bfill() 后向填充

    duplicated() 判断重复值
    df.duplicated() 判断每一行是否重复
    df.duplicated(
        subset=["date","code"]
    ) 按主键判断是否重复 可以.sum()统计重复值数量
    df.drop_duplicates() 删除重复值
'''