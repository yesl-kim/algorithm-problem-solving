class Solution:
    def romanToInt(self, s: str) -> int:
        numbers={
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000
        }
        
        res=0
        i=0
        while i<len(s)-1:
            if numbers.get(s[i:i+2]):
                res+=numbers[s[i:i+2]]
                i+=2
            else:
                res+=numbers[s[i]]
                i+=1
        if i<len(s):
            res+=numbers[s[-1]]
            
        return res