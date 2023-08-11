class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point = 0
        for num in nums:
            if num != 0:
                nums[point] = num
                point += 1
        
        for i in range(point, len(nums)):
            nums[i] = 0
        
        return nums