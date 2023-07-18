from itertools import accumulate
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,suf=list(accumulate(nums,mul)), list(accumulate(nums[::-1],mul))[::-1]
        for i in range(len(nums)):
            nums[i]=(pre[i-1] if 0<i else 1)*(suf[i+1] if i<len(nums)-1 else 1)
        return nums
        
        