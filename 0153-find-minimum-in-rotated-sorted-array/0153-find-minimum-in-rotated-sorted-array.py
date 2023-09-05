class Solution: 
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        
        target = nums[0]
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right - 1) // 2
            if nums[mid] < target:
                right = mid
            else:
                left = mid + 1
        return nums[right]
        