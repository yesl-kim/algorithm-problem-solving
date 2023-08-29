class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = 0
        res = []
        
        for i, n in enumerate(nums):
            if i + 1 == len(nums) or n + 1 != nums[i+1]:
                r = str(n) if left == i else f"{nums[left]}->{nums[i]}"
                res.append(r)
                left = i + 1
        
        return res