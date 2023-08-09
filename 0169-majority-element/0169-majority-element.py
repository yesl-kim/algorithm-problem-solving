from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
        
        n = len(nums)
        for num, c in count.items():
            if c > n / 2:
                return num