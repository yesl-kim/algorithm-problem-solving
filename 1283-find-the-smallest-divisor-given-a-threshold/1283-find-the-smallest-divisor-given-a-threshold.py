import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lt, rt = 1, max(nums)
        res = None
        check = lambda divisor: sum(math.ceil(n / divisor) for n in nums) <= threshold
        
        while lt <= rt:
            mid = (lt + rt) // 2
            if check(mid):
                res = mid
                rt = mid - 1
            else:
                lt = mid + 1

        return res