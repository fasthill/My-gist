from functools import reduce

dfs = [df_estimator, df_concat]
df_merged= reduce(lambda  left,right: pd.merge(left,right
