def get_vifs(model):
  # Note: Please import variance_inflation_factor as vif and pandas as pd before using this function.
  #        model(parameter)
  col_num = model.exog.shape[1] 
  vifs = [vif(model.exog, i) for i in range(0, col_num)]
  print(pd.DataFrame(vifs, index=model.exog_names, columns=["VIF"]))
