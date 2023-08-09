get_number = lambda word: ord(word) - 64

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        decimals = 26
        cnt = len(columnTitle) - 1
        for word in columnTitle:
            res += (decimals**cnt) * get_number(word)
            cnt -= 1
        
        return res