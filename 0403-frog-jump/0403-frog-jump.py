class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = {}
        def can_jump(pos, step) -> bool:
            stone = pos + step
            if (pos, step) in memo:
                return memo[(pos, step)]
            
            if stone == stones[-1]:
                return True
            if stone > stones[-1] or not stone in stones:
                memo[(pos, step)] = False
                return False
            
            res = any(can_jump(stone, k) for k in range(step-1, step +2) if 0 < k)
            memo[(pos, step)] = res
            return res
        
        return can_jump(0, 1)