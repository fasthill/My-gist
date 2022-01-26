# DataFrame 결측값 여부 확인, 결측값 개수 : 
'''
isnull(), notnull(), df.isnull().sum(), df.notnull().sum(), df.isnull().sum(1), df.notnull().sum(1)
'''
import pandas as pd

df = pd.DataFrame({'a': [10, None ,20, 40], 'b': [20, None, None, 30]})
df
# a	b
# 0	10.00	20.00
# 1	NaN	NaN
# 2	20.00	NaN
# 3	40.00	30.00

df.isnull() # isnull() 메소드는 관측치가 결측이면 True, 아니면 False
pd.isnull(df)
# a	b
# 0	False	False
# 1	True	True
# 2	False	True
# 3	False	False

df.notnull() # 메소드는 관측치가 결측이면 False, 아니면 True 반환. .isnull과 완전반대
pd.notnull(df) 
# 	a	b
# 0	True	True
# 1	False	False
# 2	True	False
# 3	True	True

df.isnull().sum() # 모든 열을 대상으로 null의 갯수 반환
# a    1
# b    2
# dtype: int64

df.isnull().sum().sum() # 전체 df에 있는 null 갯수 반환 (column별 null갯수을 대상으로 전체 개수 반환)
# 3

df['a'].isnull().sum() # 'a' 칼럼의 null 개수 반환
# 1

df.notnull().sum() # 모든 열을 대상으로 not null의 갯수 반환
# a    3
# b    2
# dtype: int64

df.isnull().sum(1) # 행단위로 결측치 갯수 구하기
# 0    0
# 1    2  -> 1 열에는 2개의 null 존재
# 2    1  -> 2 열에는 1개의 null 존재
# 3    0
# dtype: int64

