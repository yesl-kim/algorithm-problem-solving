class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            start,end=intervals[i]
            prev_start,prev_end=res[-1]
            if prev_end<start:
                res.append(intervals[i])
            else:
                res[-1][1]=max(prev_end,end)
        return res