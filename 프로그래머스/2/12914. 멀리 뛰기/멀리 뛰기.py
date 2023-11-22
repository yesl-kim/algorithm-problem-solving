import sys
sys.setrecursionlimit(10**7)

def solution(n):
    memo = [x if x < 3 else None for x in range(n + 1)]
    def count(n):
        if n <= 0:
            return 0
        if not memo[n]:
            memo[n] = (count(n-1) + count(n-2)) % 1234567
        return memo[n]
    return count(n) % 1234567