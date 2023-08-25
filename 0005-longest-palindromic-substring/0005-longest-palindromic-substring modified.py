class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        

        if len(s) < 2 or s == s[::-1]:
            return s
        
        res = ''
        for i in range(len(s) - 1):
                res = max(res, expand(i,i), expand(i, i+1), key=len)
        
        return res
                