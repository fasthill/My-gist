from functools import reduce

dfs = [df_lr_acc, df_sc_acc, df_dt_acc ]
df_merged = reduce(lambda  left,right: pd.merge(left,right, how='left', left_index=True, right_index=True), dfs)

                                               
df_base = df_base.merge(df2, how='left', left_index=True, right_index=True)
df_base = pd.merge(df_base,df_concat, how='outer', left_index=True, right_index=True) # 서로다른 index join

df_concat = pd.concat([df1, df2]) # df1 밑에 df2가 달림 .append와 동일. append는 더이상 사용하지 않음.


