class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        
        # find k
        for k in range(n):
            if nums[0] > nums[k]:
                break
        else:
            k += 1
        
        left, right = nums[:k], nums[k:]
        try:
            i = self.find(left, target) if left[0] <= target else self.find(right, target) + k
            return i if nums[i] == target else -1
        except:
            return -1
            
    
    def find(self, nums, target):
        l, r = 0, len(nums) - 1
        
        if nums[r] < target:
            raise
        
        while l < r:
            mid = (l + r - 1) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return r