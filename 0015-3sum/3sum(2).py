from itertools import combinations


# 1) 조합 구하기
# 2) 조건에 맞는 조합 필터링

# 1) 조건 구하기: 두 요소의 합이 되어야 하는 값
# 2) 조건에 맞는 조합 구하기

def threesum(xs):
    res = []
    
    for (i, j) in combinations(range(len(xs)), 2):
        x, y, z = xs[i], xs[j], -(xs[i] + xs[j])
        if z in set(xs[j + 1: ]):
            res.append((x, y, z))
    
    return res


# 첫 출발 (참고 코드)
# def threesum(xs):
#     return [(xs[i], xs[j], xs[k])
#             for (i, j, k) in combinations(range(len(xs)), 3)
#             if xs[i] + xs[j] + xs[k] == 0]


print(threesum([1, 2, -3, -4, -1]))

# set -> -1, 0, 1, 2, -4