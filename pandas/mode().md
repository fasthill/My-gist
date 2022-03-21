From [Python 완전정복 시리즈](https://wikidocs.net/155466)

### 14-04 최빈값 (mode)
##### DataFrame.mode(axis=0, numeric_only=False, dropna=True)
#### 개요
mode메서드는 대상 행/열의 최빈값을 구하는 메서드입니다.
최빈값이 여러개일 경우 모두 표시합니다.

#### 사용법
##### 기본 사용법
※ 자세한 내용은 아래 예시를 참고 바랍니다. 
```
df.mode(axis=0, numeric_only=False, dropna=True)
axis : {0 : index / 1 : columns} 최빈값을 구할 축 입니다.
numeric_only : True일 경우 숫자, 소수, 부울값만 있는 열에대해서만 연산을 수행합니다.
dropna : 결측치를 계산에서 제외할지 여부입니다. False일 경우 결측치도 계산에 포함됩니다.
```

#### 예시
먼저 기본적인 사용법 예시를 위해 4x4짜리 객체를 생성하겠습니다.

```
[N,T,F]=[np.NaN,True,False]
idx = ['row1','row2','row3','row4']
col = ['col1','col2','col3','col4']
data = [['A',2,'x',N],['B',2,'y',N],['C',1,'y',1],['A',N,'z',3]]
df = pd.DataFrame(data,idx,col)
print(df)
>>
     col1  col2 col3  col4
row1    A   2.0    x   NaN
row2    B   2.0    y   NaN
row3    C   1.0    y   1.0
row4    A   NaN    z   3.0
```

#### 기본적인 사용법
mode메서드를 사용하면 각 열에 대해서 최빈값이 인덱스 0에 출력됩니다.

만약 최빈값이 여러개일 경우 갯수만큼 인덱스가 생성되어 출력됩니다.

이 때, 최빈값 이외의 값은 NaN을 출력합니다.

<span style='color:blue'> 촤빈값만 표시되고 그 이외는 모두 NaN </span>

<span style='color:blue'> 최빈항목이 많을 경우 모두 표시, 예) col4 의경우 1.0과 3.0이 각각 1개로 최빈값이므로 동시에 표시 </span>

```
print(df.mode())
  col1  col2 col3  col4
0    A   2.0    y   1.0
1  NaN   NaN  NaN   3.0

# col4의 최빈값이 1과 3으로 두개이기 때문에 두개 다 출력, 나머지는 최빈값이 하나이므로 1행에는 NaN출력
```

#### dropna인수의 사용
기본적으로 결측치는 최빈값 계산에서 제외됩니다. dropna= True로 할 경우 결측치도 계산에 포함되며,

결측치가 제일 많을 경우 최빈값은 결측치가 됩니다.
```
print(df.mode(dropna=False))
>>
  col1  col2 col3  col4
0    A   2.0    y   NaN
# col4에는 NaN이 가장 많으므로 최빈값이 NaN으로 계산됨.
```

#### numeric_only인수의 사용
numeric_only인수가 True인 경우 숫자 or bool형태가 아닌 자료형을 갖는 열은 계산에서 제외됩니다.
```
print(df.mode(numeric_only=True))
>>
   col2  col4
0   2.0   1.0
1   NaN   3.0
# col1, col3에는 문자열 형식이 존재하므로 계산에서 제외됨.
```
