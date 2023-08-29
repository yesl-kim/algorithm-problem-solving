from functools import reduce

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return reduce(lambda acc, i: acc + min(nums[i], nums[i+1]), range(0, len(nums), 2), 0)