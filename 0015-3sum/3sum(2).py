from itertools import combinations
from collections import defaultdict


# 1) 조합 구하기
# 2) 조건에 맞는 조합 필터링

# 1) 조건 구하기: 두 요소의 합이 되어야 하는 값
# 2) 조건에 맞는 조합 구하기

def threesum(xs):

    sums=defaultdict(list)
    for i, v in enumerate(xs):
        sums[v].append(i)

    def has(i, j, z):
        for k in sums[z]: # (1)
            if k != i and k != j:
                sums[z].remove(k) # (2)
                return True
        return False
    
    res = set()
    for (i, j) in combinations(range(len(xs)), 2):
        x, y, z = xs[i], xs[j], -(xs[i] + xs[j])
        if has(i, j, z):
            res.add(tuple(set([x,y,z]))) # (3)
    
    return list(res)

def threesum(xs):
    res = []

    def findAfter(i, j, z):
        return z in set(xs[max(i, j) + 1: ])
    
    for (i, j) in combinations(range(len(xs)), 2):
        x, y, z = xs[i], xs[j], -(xs[i] + xs[j])
        if findAfter(i, j, z):
            res.append((x, y, z))
    
    return res


# 첫 출발 (참고 코드)
def threesums(xs):
    return [(xs[i], xs[j], xs[k])
            for (i, j, k) in combinations(range(len(xs)), 3)
            if xs[i] + xs[j] + xs[k] == 0]


print(threesum([1, 2, -3, -4, -1, 0]))
print(threesums([1, 2, -3, -4, -1, 0]))

# set -> -1, 0, 1, 2, -4