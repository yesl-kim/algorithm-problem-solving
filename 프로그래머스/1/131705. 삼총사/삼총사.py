from collections import defaultdict
from itertools import combinations
from bisect import bisect_right

def solution(numbers):
    indices = defaultdict(list)
    for i, n in enumerate(numbers):
        indices[n].append(i)

    def count_after(x, v):
        arr = indices[x]
        if not arr or arr[-1] <= v:
            return 0
        
        i = bisect_right(arr, v)
        if len(arr) <= i:
            return 0
        
        return len(arr) - i
        

    cnt = 0
    for i, j in combinations(range(len(numbers)), 2):
        x = -(numbers[i] + numbers[j])
        cnt += count_after(x, j)
    
    return cnt