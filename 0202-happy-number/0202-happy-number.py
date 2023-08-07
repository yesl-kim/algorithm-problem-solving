from collections import defaultdict
from functools import reduce

class Solution:
    def isHappy(self, n: int) -> bool:
        memo = defaultdict(int)
        
        while n != 1 and not memo[n]:
            square = reduce(lambda acc, cur: acc + int(cur)**2, str(n), 0)
            memo[n] = square
            n = square
        
        return n == 1