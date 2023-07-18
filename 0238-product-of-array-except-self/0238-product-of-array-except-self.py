from itertools import accumulate
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n,suf=len(nums),1
        res=[1]*n
        for i in range(1,n):
            res[i]=res[i-1]*nums[i-1]
        for i in range(n-1,-1,-1):
            res[i]*=suf
            suf*=nums[i]
        return res