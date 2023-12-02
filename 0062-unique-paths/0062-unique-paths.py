from functools import lru_cache

def memoize(fn):
    cache = {}
    def memoizer(*args, **kargs):
        key = str(args) + str(kargs)
        if not key in cache:
            cache[key] = fn(*args, **kargs)
        return cache[key]
    return memoizer
        

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache
        def paths(x, y):
            if not (0 <= x < m) or not (0 <= y < n):
                return 0
            
            if x == m - 1 and y == n - 1:
                return 1
            
            return paths(x, y + 1) + paths(x + 1, y)
        return paths(0, 0)