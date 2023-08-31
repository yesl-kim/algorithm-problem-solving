class Solution:
    def move(self, nums, left, right, val):
        while left < len(nums) and nums[left] != val:
            left += 1
        
        while 0 <= right and nums[right] == val:
            right -= 1
        
        return left, right
    
    
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = self.move(nums, 0, len(nums) - 1, val)

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = self.move(nums, left, right, val)
        
        return left