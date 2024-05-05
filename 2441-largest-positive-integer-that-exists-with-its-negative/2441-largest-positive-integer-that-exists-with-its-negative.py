class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        k = -1
        past = set()
        for x in nums:
            if -x in past:
                k = max(k, abs(x))
            else:
                past.add(x)
        return k