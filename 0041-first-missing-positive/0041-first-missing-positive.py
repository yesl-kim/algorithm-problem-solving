class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        _min, _max = min(nums), max(nums)
        if _min > 1 or _max < 1:
            return 1
        
        n = len(nums)
        if _max - _min + 1 == n:
            return _max + 1
        
        for x in range(1, n + 1):
            if not x in nums:
                return x