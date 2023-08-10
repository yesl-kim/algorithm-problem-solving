class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        
        for i in range(n):
            subs = { s[i] }
            
            for j in range(i+1, n):
                if n - i < res:
                    return res
                if s[j] in subs:
                    break
                else:
                    subs.add(s[j])
            res = max(res, len(subs))
        
        return res