from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = None
        nums = [(-x, x) for x in nums]
        heapify(nums)
        for _ in range(k):
            _, res = heappop(nums)
        return res