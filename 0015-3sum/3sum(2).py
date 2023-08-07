from itertools import combinations
from collections import defaultdict


# 그럼 왜 마지막 인덱스만 저장하는게 아니라 모든 인덱스를 다 담아야할까? 어차피 마지막 인덱스만 확인할텐데?
# 사용한 요소를 제거하지도 않는데??


def threesum(xs):
    xs.sort()
    
    index = defaultdict(int)
    for i, v in enumerate(xs):
        index[v] = i

    res = set()
    for (i, j) in combinations(range(len(xs)), 2):
        x, y, z = xs[i], xs[j], -(xs[i] + xs[j])
        if j < index[z]:
            res.add((x, y, z))
    
    return res

has_greater = lambda value, arr: arr and value < arr[-1]

# def threesum(xs):
#     xs.sort()
#     indices = defaultdict(list)
#     for i, v in enumerate(xs):
#         indices[v].append(i)

#     res = []
#     for (i, j) in combinations(range(len(xs)), 2):
#         x, y, z = xs[i], xs[j], -(xs[i] + xs[j])
#         if has_greater(j, indices[z]):
#             res.append((x, y, z))
    
#     return set(res)


# 첫 출발 (참고 코드)
def threesums(xs):
    return [(xs[i], xs[j], xs[k])
            for (i, j, k) in combinations(range(len(xs)), 3)
            if xs[i] + xs[j] + xs[k] == 0]

output = threesum([-1,0,1,2,-1,-4,-2,-3,3,0,4])
expected = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
# output = threesum([-1,0,1,0])
# expected = [[-1,0,1]]

print(f"output: {len(output)} => {output}")
print(f"expected: {len(expected)} => {expected}")
