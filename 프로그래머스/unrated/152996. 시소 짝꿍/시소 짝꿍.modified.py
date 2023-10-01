from collections import defaultdict
from itertools import permutations
from bisect import bisect_right

def solution(weights):
    indices = defaultdict(list)
    for i, w in enumerate(weights):
        indices[w].append(i)
    
    def count(arr, i):
         if not arr or arr[-1] <= i:
             return 0

         return len(arr) - bisect_right(arr, i)
    
    cnt = 0
    for i, x in enumerate(weights):
        cnt += count(i, indices[x])
        for m, d in permutations((2,3,4), 2):
            y = x * m / d
            cnt += count(i, indices[y])
    return cnt