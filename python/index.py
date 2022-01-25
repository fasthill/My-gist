import numpy as np
alist = ['hi!', 'hello', 'bye', 'hello', 'hi!']

alist.index('hello')
# 1

# 중복되는 원소들의 인덱스 모두 찾기 (numpy.where)
anp = np.array(alist)
np.where(anp == 'hello')
# (array([1, 3], dtype=int64),)

np.where(anp == 'hello')[0]
# array([1, 3], dtype=int64)

np.where(anp == 'hello')[0][0]
# 1
