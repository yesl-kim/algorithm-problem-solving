from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = defaultdict(int)
        for x in s:
            counts[x] += 1
            
        for x in t:
            if not counts[x]:
                return False
            
            counts[x] -= 1
        
        for n in counts.values():
            if n > 0:
                return False
        else:
            return True