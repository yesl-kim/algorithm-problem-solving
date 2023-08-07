from itertools import combinations
from collections import defaultdict


# 1) 조합 구하기
# 2) 조건에 맞는 조합 필터링

# 1) 조건 구하기: 두 요소의 합이 되어야 하는 값
# 2) 조건에 맞는 조합 구하기

def threesum(xs):
    indices=defaultdict(list)
    for i, v in enumerate(xs):
        indices[v].append(i)

    def hasAfter(i, j, z):
        after = max(i, j)
        left, right = 0, len(indices[z]) - 1

        if not indices[z] or indices[z][right] < after:
            return False

        while left <= right:
            cur = (left + right) // 2
            if indices[z][cur] <= after:
                left = cur + 1
            else:
                right = cur - 1
                index = cur
        
        del indices[z][index]
        return True
    
    res = []
    for (i, j) in combinations(range(len(xs)), 2):
        x, y, z = xs[i], xs[j], -(xs[i] + xs[j])
        if hasAfter(i, j, z):
            res.append((x, y, z))
    
    return res


# hasAfter 에서 사용한 요소를 제거하면, res에 추가할 때 중복을 신경쓸 필요가 없고 => hasAfter 순수함수가 아님
# hasAfter 에서 사용한 요소를 제거하지 않으면, res에 추가할 때 중복 처리를 해줘야함 => hasAfter 순수함수


# 첫 출발 (참고 코드)
def threesums(xs):
    return [(xs[i], xs[j], xs[k])
            for (i, j, k) in combinations(range(len(xs)), 3)
            if xs[i] + xs[j] + xs[k] == 0]


# print(threesum([1, 2, -3, -4, -1, 0]))
# print(threesums([1, 2, -3, -4, -1, 0]))
# print(threesums([2,-2,0,-4,2,8,-10]))
# print(threesum([2,-2,0,-4,2,8,-10]))
print(threesum([-1,0,1,2,-1,-4]))
print(threesums([-1,0,1,2,-1,-4]))

# set -> -1, 0, 1, 2, -4