from collections import defaultdict

# lambda이용하여 초기값 지정
d_dict = defaultdict(lambda: 'school')
d_dict["str"]
# 'school'

d_dict = defaultdict(int)
d_dict["a"]
# 0
d_dict
# defaultdict(int, {'a': 0})

# 최초 value가 없어도 사칙연산 가능
d_dict = defaultdict(int)
d_dict["a"] += 10
d_dict
# defaultdict(int, {'a': 10})
