class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counters = defaultdict(int)
        cnt = 0
        
        for t in time:
            opposite = (60 - (t % 60)) % 60
            cnt += counters[opposite]
            counters[t % 60] += 1
        
        return cnt