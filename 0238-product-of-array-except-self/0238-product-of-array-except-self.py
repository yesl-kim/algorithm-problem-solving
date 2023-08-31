from itertools import accumulate
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul1 = list(accumulate(nums, mul))
        mul2 = list(accumulate(nums[::-1], mul))[::-1]
        return [(mul1[i-1] if i else 1) * (mul2[i+1] if i + 1 < len(nums) else 1) for i in range(len(nums))]