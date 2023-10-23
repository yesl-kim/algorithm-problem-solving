from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [x[0] for x in sorted(c.items(), key=lambda x: x[1], reverse=True)[:k]]