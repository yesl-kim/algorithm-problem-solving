from collections import defaultdict
from functools import reduce

class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        
        while n != 1 and n not in memo:
            memo.add(n)
            n = reduce(lambda acc, cur: acc + int(cur)**2, str(n), 0)
        
        return n == 1