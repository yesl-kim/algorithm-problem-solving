from itertools import accumulate
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,suf,n=list(accumulate(nums,mul)), list(accumulate(nums[::-1],mul))[::-1],len(nums)
        return [(pre[i-1] if i else 1)*(suf[i+1] if i+1<n else 1) for i in range(n)]
        
        