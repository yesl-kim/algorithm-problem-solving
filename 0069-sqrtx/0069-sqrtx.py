class Solution:
    def mySqrt(self, x: int) -> int:
        left, right=0, x
        res=0
        
        while left<=right:
            mid=(left+right)//2
            square = mid**2
            
            if square==x:
                return mid
            if square > x:
                right=mid-1
            else:
                res=mid
                left=mid+1
                
        return res