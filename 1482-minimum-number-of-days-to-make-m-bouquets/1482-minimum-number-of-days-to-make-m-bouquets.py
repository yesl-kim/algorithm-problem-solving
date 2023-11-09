class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        def check(x):
            bouquets = 0
            flowers = 0
            for day in bloomDay:
                if day <= x:
                    flowers += 1
                else:
                    bouquets += (flowers // k)
                    flowers = 0
            
            bouquets += (flowers // k)
            return bouquets >= m
            
        # 0 < x <= max(bloomDay)
        lo, hi = 1, max(bloomDay)
        res = None
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res if res else -1