class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        check = [0] * (len(nums) + 1)
        for n in nums:
            check[n] = 1
        
        for num, ch in enumerate(check):
            if not ch:
                return num
        