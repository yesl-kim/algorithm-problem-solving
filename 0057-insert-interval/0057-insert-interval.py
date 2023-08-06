class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert
        intervals.append(newInterval)
        
        # sort
        intervals.sort(key=lambda x: x[0])
        
        # merge
        i = 1
        while i < len(intervals):
            prev = intervals[i-1]
            cur = intervals[i]
            
            if cur[0] <= prev[1]:
                prev[1] = max(prev[1], cur[1])
                intervals.remove(cur)
            else:
                i+=1
        
        return intervals