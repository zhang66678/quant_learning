'''merge()与数据对齐

   how="left 保留都有的键 交集
   inner 左表全部和右表匹配
   right 
   outer 所有 并集"
'''

import pandas as pd

price_df = pd.DataFrame({
    "date":[2023-1-1,2023-1-1,2023-1-2,2023-1-2],
    "code":["A","B","A","B"],
    "close":[10,20,11,19]
})

factor_df = pd.DataFrame({
      "date":[2023-1-1,2023-1-1,2023-1-2],
      "code":["A","B","A"],
      "factor":[0.2,0.1,0.3]
   })

result = pd.merge(
    price_df,
    factor_df,
    on = ["date", "code"],
    how = "left"
)
print(result)
