from functools import reduce

dfs = [df_lr_acc, df_sc_acc, df_dt_acc ]
df_merged = reduce(lambda  left,right: pd.merge(left,right, how='left', left_index=True, right_index=True), dfs)

                                               
df_base = df_base.merge(df2, how='left', left_index=True, right_index=True)
