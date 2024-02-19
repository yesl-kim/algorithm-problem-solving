from itertools import combinations
from collections import defaultdict
from bisect import bisect_right, bisect_left

def solution(info, query):
    groups = defaultdict(list)
    for x in info:
        *values, score = x.split()
        score = int(score)
        for x in range(5):
            for options in combinations(range(4), x):
                key = " and ".join((value if i not in options else '-' for i, value in enumerate(values)))
                i = bisect_right(groups[key], score)
                groups[key].insert(i, score)

    res = []
    for q in query: # 100,000 (10만)
        q, score = q.rsplit(' ', 1)
        score = int(score)
        group = groups[q]
        i = bisect_left(group, score)
        cnt = len(group) - i
        res.append(cnt)

    return res