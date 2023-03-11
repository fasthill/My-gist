When to use split vs gain for plot_importance?
 - gain을 위주로 사용. 큰차이 없음

https://github.com/microsoft/LightGBM/issues/4255
  
  다음과 같이 DataFrame으로 전환하여 사용하면 편함.
  df_sel = pd.DataFrame(model.booster_.feature_importance(importance_type='gain'), 
                      index=data.columns, columns=['importance']).sort_values(by='importance', 
                                                                              ascending=False)
  
  model.booster_.feature_importance(importance_type='split')
# split을 사용하는 feature
