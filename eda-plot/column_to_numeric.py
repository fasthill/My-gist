import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

url_auto = 'https://raw.githubusercontent.com/fasthill/My-gist/main/data/Automobile_data.csv'
df = pd.read_csv(url_auto)

print("Object columns:", df.select_dtypes('object').columns)
print("Number columns:", df.select_dtypes('number').columns)

# df.info()에서 dtype이 'object"로 확인디나 실제로는 number인 column을 숫자열로 변환
for colname in df.select_dtypes('object').columns:
    if df[colname].str.contains(r'\d+.?\d*[^a-zA-Z]').any(): # 숫자(.숫자)이면서 문자로 이어지지 않는 형식
        df[colname] = pd.to_numeric(df[colname], errors='coerce').astype('float')

X = df.copy()
y = X.pop('price')

# Label encoding for categoricals
for colname in X.select_dtypes("object"):
    X[colname], _ = X[colname].factorize()

print("Object columns:", df.select_dtypes('object').columns)
print("Number columns:", df.select_dtypes('number').columns)

