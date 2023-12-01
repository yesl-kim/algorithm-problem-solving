import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor):
            return sum(math.ceil(n / divisor) for n in nums) <= threshold
        
        lt, rt = 1, max(nums)
        res = None
        while lt <= rt:
            mid = (lt + rt) // 2
            if check(mid):
                # 최솟값을 찾음
                res = mid
                rt = mid - 1
            else:
                lt = mid + 1

        return res