class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        
        def combine(c):
            total = sum(c)
            if total > target:
                return
            if total == target:
                res.add(tuple(sorted(c)))
                return
            
            for x in candidates:
                combine(c + [x])
        
        combine([])
        return res
                