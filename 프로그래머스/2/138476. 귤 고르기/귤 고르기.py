from collections import Counter

def solution(k, tangerine):
    total = 0
    res = 0
    for t, cnt in Counter(tangerine).most_common():
        total += cnt
        res += 1
        if total >= k:
            return res