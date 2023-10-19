from collections import defaultdict
from bisect import bisect_left

def solution(s):
    res = []
    last_index = {}
    for i, x in enumerate(s):
        if x in last_index:
            res.append(i - last_index[x])
        else:
            res.append(-1)
        last_index[x] = i
    return res
        
        
            