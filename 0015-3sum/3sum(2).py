from itertools import combinations
from collections import Counter


# 그럼 왜 마지막 인덱스만 저장하는게 아니라 모든 인덱스를 다 담아야할까? 어차피 마지막 인덱스만 확인할텐데?
# 사용한 요소를 제거하지도 않는데??
# 변경에 쉽게 대응하기 위해서인가? 요소 중복, 조합 중복 등은 쉽게 변경 가능한 세부조건들이니까..
# 그럼 본질은 뭘까

# occasions로 풀어보기
# - 요소 중복 막기
# - 조합 중복 막기
class Occtools():
    def __init__(self, arr):
        self.data = Counter(arr)
        self.actions = []

    @property
    def occasions(self):
        return self.data


    def __enter__(self):
        print('enter')
        return self
    

    def use(self, *keys):
        for key in keys:
            self.data[key] -= 1
            self.actions.append(key)


    def __exit__(self, *args):
            for x in self.actions:
                self.data[x] += 1
            self.actions = []


def threesum(nums):
    occtools = Occtools(nums[2:])
    occasions = occtools.occasions

    res = []
    for (i, j) in combinations(range(len(nums)-1), 2): # o(n^2)
        with occtools:
            x, y, z = nums[i], nums[j], -(nums[i] + nums[j])
            occtools.use(x, y)
            if 0 < occasions[z]:
                res.append((x, y, z))
    
    return set([tuple(sorted(c)) for c in res])




has_greater = lambda value, arr: arr and value < arr[-1]


# 첫 출발 (참고 코드)
def threesums(xs):
    return [(xs[i], xs[j], xs[k])
            for (i, j, k) in combinations(range(len(xs)), 3)
            if xs[i] + xs[j] + xs[k] == 0]

input = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
# output = threesum([-1,0,1,2,-1,-4,-2,-3,3,0,4])
expected = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
# output = threesum([-1,0,1,0])
# expected = [[-1,0,1]]
# output = threesum([-1,1,0,-1,1,0])

# print(f"output: \n=> {len(output)}개, \n=> {output}")
# print(f"expected: \n=> {len(expected)}개, \n=> {expected}")

occ = Counter(input)
occtools = Occtools(input)
occ = occtools.occasions
# print(occ)
# keys = list(occ.keys())
# # key = keys[0]
# key = keys[:3]
# with occtools:
#     occtools.use(*key)
#     for o in occ.items():
#         print(o)

# print('finally')
# for o in occ.items():
#         print(o)

