from collections import defaultdict
from itertools import permutations

def solution(weights):
    indices = defaultdict(list)
    for i, w in enumerate(weights):
        indices[w].append(i)
    
    def count(i, arr):
        if not arr or arr[-1] <= i:
            return 0
        
        l = len(arr)
        left, right = 0, l - 1
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= i:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
        
        return l - res
    
    cnt = 0
    for i, x in enumerate(weights):
        cnt += count(i, indices[x])
        for m, d in permutations((2,3,4), 2):
            y = x * m / d
            cnt += count(i, indices[y])
    return cnt