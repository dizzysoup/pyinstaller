import os,importlib
import xgboost as xgb
import pandas as pd

df= pd.read_csv(r'2021test0831.csv')
X = df.iloc[:,1:14]

p =xgb.XGBRegressor()
p.load_model('mean.model')

p = p.predict(X)

col = ['編號','預測值']
z = pd.DataFrame(columns=col)
z['預測值'] = p
h = len(z)
z['編號'] = list(range(1,h+1))
print(z)

z.to_excel('2110999_TestResult.xlsx',index = False)
