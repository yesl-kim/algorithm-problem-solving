def solution(nums):
    kinds = set(nums)
    k, n = len(kinds), len(nums) // 2
    return k if k < n else n