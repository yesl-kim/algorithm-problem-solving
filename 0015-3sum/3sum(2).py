from itertools import combinations
from collections import Counter

class Lock():
    def __init__(self, x, occ) -> None:
        self.key = x
        self.occasions = occ

    def __enter__(self):
        self.occasions[self.key] -= 1
    
    def __exit__(self, *args):
        self.occasions[self.key] += 1


lock = lambda occ: lambda x: Lock(x, occ)


def threesum(nums):
    occasions = Counter(nums)
    _Lock = lock(occasions)

    res = []
    for (i, j) in combinations(range(len(nums)), 2):
        x, y, z = nums[i], nums[j], -(nums[i] + nums[j])
        with _Lock(x), _Lock(y):
            if 0 < occasions[z]:
                res.append((x, y, z))
    
    return set([tuple(sorted(c)) for c in res])


# 첫 출발 (참고 코드)
def threesums(xs):
    return [(xs[i], xs[j], xs[k])
            for (i, j, k) in combinations(range(len(xs)), 3)
            if xs[i] + xs[j] + xs[k] == 0]