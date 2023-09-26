from collections import defaultdict
from functools import reduce
from operator import mul

def solution(clothes):
    hash = defaultdict(list)
    for name, kind in clothes:
        hash[kind].append(name)
    
    return reduce(mul, [len(x) + 1 for x in hash.values()], 1) - 1
            