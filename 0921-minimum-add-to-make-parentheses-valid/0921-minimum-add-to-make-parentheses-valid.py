class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens, closes = 0, 0
        for p in s:
            if p == '(':
                opens += 1
            else:
                if 0 < opens:
                    opens -= 1
                else:
                    closes += 1
        return opens + closes