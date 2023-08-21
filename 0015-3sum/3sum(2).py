from itertools import combinations
from collections import Counter

# 이해가 안감,,,,,,
# Lock이 occasions를 따로 참조할 수 있나..?
# Lock의 역할이 뭐지..?
# 사용 후 원복 자체를 추상화하는건가..? 사용도???
# i) occasions[x]를 사용하고(-1) 다시 원복(+1) => occasions 참조 필요 => 외부와의 의존성이 너무 높아지는데...?
# ii) 

# 이해를 못한 것: Lock이 사용 후 원복하는 걸 말하는 건가? 따로 occasions[x] -= 1 할 필요없이?
# 막혔던 것: Lock에서 기존 동작을 하려면 occasions의 참조가 필요한데, 이 방법이 맞는건가? 
#   - 이런 동작이면 Use라는 이름이 더 맞지 않나?
#   - 기존 동작이 수정되어야 하는건가?

lock = lambda occ: lambda x: Lock(x, occ)
class Lock():
    def __init__(self, x, occ) -> None:
        self.key = x
        self.occasions = occ

    def __enter__(self):
        self.occasions[self.key] -= 1
    
    def __exit__(self, *args):
        self.occasions[self.key] += 1


def threesum(nums):
    occasions = Counter(nums[2:])
    _Lock = lock(occasions)

    res = []
    for (i, j) in combinations(range(len(nums)-1), 2): # o(n^2)
        x, y, z = nums[i], nums[j], -(nums[i] + nums[j])
        with _Lock(x), _Lock(y):
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
output = threesum([-1,0,1,2,-1,-4,-2,-3,3,0,4])
expected = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
# output = threesum([-1,0,1,0])
# expected = [[-1,0,1]]
# output = threesum([-1,1,0,-1,1,0])

print(f"output: \n=> {len(output)}개, \n=> {output}")
print(f"expected: \n=> {len(expected)}개, \n=> {expected}")

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

