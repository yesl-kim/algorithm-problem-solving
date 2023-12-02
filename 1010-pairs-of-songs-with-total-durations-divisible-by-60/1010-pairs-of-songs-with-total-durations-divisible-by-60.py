from collections import defaultdict
from bisect import bisect_right

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        indices = defaultdict(list)
        for i, t in enumerate(time):
            indices[t].append(i)
            
        def range_x(t):
            for total in count(60, 60):
                x = total - t
                if x <= 0:
                    continue
                if x > 500:
                    break
                yield x
            
        def find_after(x, i):
            # i 뒤에 있는 x의 개수를 반환
            # = indices[x] 중에 i 보다 큰 수의 개수
            if not x in indices:
                return 0
            
            arr = indices[x]
            if arr[-1] < i:
                return 0
            
            return len(arr) - bisect_right(arr, i)
                
            
        cnt = 0
        for i, t in enumerate(time):
            for x in range_x(t):
                cnt += find_after(x, i)
                
        return cnt