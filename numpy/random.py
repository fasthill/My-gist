import numpy as np

''' 
random.choice(a, size=None, replace=True, p=None) 
Generates a random sample from a given 1-D array
'''
np.random.choice(5, 3) # Generate a uniform random sample from np.arange(5) of size 3:
# array([0, 3, 4])  # 중복허용

np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0]) # p 다섯개가 나타날 확률 합은 1. 
# 중복허용. 0일 확률 0.1, 1일 확률 0, 2일 확률 0.3...
# array([3, 3, 0])

np.random.choice(5, 3, replace=False) # 중복허용하지 않음. 순서대로 번호 뽑기
# array([3,1,0]) 
#This is equivalent to np.random.permutation(np.arange(5))[:3]

np.random.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0]) 
#Generate a non-uniform random sample from np.arange(5) of size 3 without replacement:

'''
random.rand(d0, d1, ..., dn)
Create an array of the given shape and populate it with random samples 
from a uniform distribution over [0, 1). 0 이상 1 미만
'''
np.random.rand(3,2)
# array([[ 0.14022471,  0.96360618],  
#        [ 0.37601032,  0.25528411],  
#        [ 0.49313049,  0.94909878]])

'''
random.randint(low, high=None, size=None, dtype=int)
Return random integers from low (inclusive) to high (exclusive).
'''
np.random.randint(2, size=10)
# array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0])
np.random.randint(1, size=10)
# array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
np.random.randint(5, size=(2, 4))
# array([[4, 0, 2, 1], 
#        [3, 2, 2, 0]])


'''
random.randn(d0, d1, ..., dn)
Return a sample (or samples) from the “standard normal” distribution.
mean: 0, std: 1
'''
np.random.randn()
# 2.1923875335537315
np.random.randn(2, 4) # 2 by 4 array
# array([[-1.802997  ,  3.2877993 ,  0.28606533, -1.33086591],
#        [ 0.14336082,  0.10763838,  0.4708106 ,  0.93318335]])

# For random samples from , use:
# sigma * np.random.randn(...) + mu  # 표준편차와 평균을 대입하여 표준분포 난수 생성
3 + 2.5 * np.random.randn(2, 4) # Two-by-four array of samples from N(3, 6.25):
# 표준편차 2.5, 평균 3인 난수 생성
# array([[2.44846027, 5.0417493 , 3.7766451 , 3.61090348],
#        [2.53702783, 6.65883557, 3.74043326, 4.70151242]])


'''
random.random(size=None)
Return random floats in the half-open interval [0.0, 1.0). 0.0 이상 1.0 미만
'''
np.random.random((2,3)) #  == np.random.rand(2,3)
# array([[0.37689245, 0.83643531, 0.45999588],
#        [0.72119264, 0.54723559, 0.53892759]])
# == np.random.random([2,3])

'''
numpy.random.uniform(low=0.0, high=1.0, size=None)
Draw samples from a uniform distribution.
'''
np.random.uniform(0.0001, 0.001)


'''
random.permutation(x)
Randomly permute a sequence, or return a permuted range.
'''
np.random.permutation(10)  # 임의의 순서대로 재배치
# array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6]) 
np.random.permutation([1, 4, 9, 12, 15]) # 현재 리스트를 임의의 순서대로 재배치
# array([15,  1,  9,  4, 12]) 

arr = np.arange(9).reshape((3, 3))
np.random.permutation(arr)
# array([[6, 7, 8], 
#        [0, 1, 2],
#        [3, 4, 5]])

'''
random.shuffle(x)
Modify a sequence in-place by shuffling its contents.
random.permutation은 원자료를 바꾸지 않으나 shffule은 inplace로 바꿈
'''
arr = np.arange(10)
np.random.shuffle(arr)
arr  # arr이 바꾸어 있음
# [1 7 5 2 9 4 3 6 0 8] # random
np.random.permutation(arr) # arr 자체는 바뀌지 않음.
