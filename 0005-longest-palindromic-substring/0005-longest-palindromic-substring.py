class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        res = ''
        for i in range(len(s)):
            for size in range(2):
                left, right = i, i + size
                while 0 <= left and right < len(s) and s[left] == s[right]:
                    if len(res) < right - left + 1:
                        res = s[left: right + 1]
                    left -= 1
                    right += 1
        
        return res
                