from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 8)

def solution(n):
    @lru_cache
    def F(n):
        if n < 2:
            return n
        
        return F(n-1) + F(n-2)
    
    return F(n) % 1234567