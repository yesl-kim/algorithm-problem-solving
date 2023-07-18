from itertools import accumulate
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n,pre,suf=len(nums),1,1
        res=[1]*n
        for i in range(n):
            res[i]*=pre
            pre*=nums[i]
            res[-1-i]*=suf
            suf*=nums[-1-i]
        return res