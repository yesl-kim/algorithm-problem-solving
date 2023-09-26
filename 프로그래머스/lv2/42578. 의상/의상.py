from collections import defaultdict, Counter
from functools import reduce
from operator import mul

def solution(clothes):
    clothes = Counter([kind for _, kind in clothes])
    return reduce(mul, [x + 1 for x in clothes.values()], 1) - 1
            