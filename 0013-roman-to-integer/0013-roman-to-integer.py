class Solution:
    def romanToInt(self, s: str) -> int:
        numbers={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        res=0
        i=0
        n=len(s)
        while i<n-1:
            if numbers[s[i]]>=numbers[s[i+1]]:
                res+=numbers[s[i]]
                i+=1
            else:
                res+=(numbers[s[i+1]]-numbers[s[i]])
                i+=2
        if i<n:
            res+=numbers[s[i]]
        return res