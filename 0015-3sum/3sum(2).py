from itertools import combinations
from collections import Counter


# 그럼 왜 마지막 인덱스만 저장하는게 아니라 모든 인덱스를 다 담아야할까? 어차피 마지막 인덱스만 확인할텐데?
# 사용한 요소를 제거하지도 않는데??
# 변경에 쉽게 대응하기 위해서인가? 요소 중복, 조합 중복 등은 쉽게 변경 가능한 세부조건들이니까..
# 그럼 본질은 뭘까

# occasions로 풀어보기
# - 요소 중복 막기
# - 조합 중복 막기
def threesum(nums):
    occasions = Counter(nums[2:])

    res = []
    for (i, j) in combinations(range(len(nums)-1), 2): # o(n^2)
        x, y, z = nums[i], nums[j], -(nums[i] + nums[j])
        occasions[x]-=1
        occasions[y]-=1
        if 0 < occasions[z]:
            res.append((x, y, z))
        occasions[x]+=1
        occasions[y]+=1
    
    return set([tuple(sorted(c)) for c in res])

has_greater = lambda value, arr: arr and value < arr[-1]


# 첫 출발 (참고 코드)
def threesums(xs):
    return [(xs[i], xs[j], xs[k])
            for (i, j, k) in combinations(range(len(xs)), 3)
            if xs[i] + xs[j] + xs[k] == 0]

output = threesum([-1,0,1,2,-1,-4,-2,-3,3,0,4])
expected = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
# output = threesum([-1,0,1,0])
# expected = [[-1,0,1]]
# output = threesum([-1,1,0,-1,1,0])

print(f"output: \n=> {len(output)}개, \n=> {output}")
print(f"expected: \n=> {len(expected)}개, \n=> {expected}")
