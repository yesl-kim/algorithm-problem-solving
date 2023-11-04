class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        def check(x):
            s, e = 0, 1
            adj_flowers_cnt = []
            bloomed = lambda i: bloomDay[i] <= x
            while s < n and e < n:
                while s < n and not bloomed(s):
                    s += 1

                e = s
                while e < n and bloomed(e):
                    e += 1
                
                adj_flowers_cnt.append(e - s)
                s = e + 1

            if sum(adj_flowers_cnt) < m * k:
                return False
            
            cnt = sum(cnt // k for cnt in adj_flowers_cnt)
            return cnt >= m
            
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