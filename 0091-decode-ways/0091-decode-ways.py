class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache
        def count(s):
            if not s:
                return 1
            if s.startswith('0'):
                return 0
            
            if len(s) > 1 and int(s[:2]) <= 26:
                return count(s[1:]) + count(s[2:])
            else:
                return count(s[1:])
        
        return count(s)