from itertools import combinations
from collections import Counter, defaultdict


class Counter:
    class Lock:
        def __init__(self, x, occ) -> None:
            self.key = x
            self.occasions = occ

        def __enter__(self):
            self.occasions[self.key] -= 1
        
        def __exit__(self, *args):
            self.occasions[self.key] += 1


    def __init__(self, arr) -> None:
        self.data = defaultdict(int)
        for x in arr:
            self.data[x] += 1

    def has(self, key):
        return 0 < self.data[key]

    def use(self, key):
        if not self.has(key):
            raise
        return self.Lock(key, self.data)


def threesum(nums):
    occasions = Counter(nums)

    res = []
    for (i, j) in combinations(range(len(nums)), 2):
        x, y, z = nums[i], nums[j], -(nums[i] + nums[j])
        try:
            with occasions.use(x), occasions.use(y), occasions.use(z):
                res.append((x, y, z))
        except:
            pass
    
    return set([tuple(sorted(c)) for c in res])



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