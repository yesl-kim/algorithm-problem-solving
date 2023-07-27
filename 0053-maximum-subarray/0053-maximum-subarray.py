from itertools import accumulate

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return nums[0]
        
        sums=list(accumulate(nums))
        min=0
        res=max(nums)
        for i in range(n):
            if sums[i]<min:
                min=sums[i]
            else:
                res=max(res,sums[i],sums[i]-min)
        return res