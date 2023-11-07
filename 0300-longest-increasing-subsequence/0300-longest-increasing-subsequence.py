from collections import defaultdict

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = list(range(len(nums)))
        for i in range(len(nums) -1, -1, -1):
            x = nums[i]
            subs_len = 0
            for j in range(i + 1, len(nums)):
                y = nums[j]
                if x < y and subs_len < dp[j]:
                    subs_len = dp[j]
            dp[i] = subs_len + 1
        return max(dp)