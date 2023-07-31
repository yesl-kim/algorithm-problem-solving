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
        key=s
        while key:
            if numbers.get(key):
                res+=numbers[key]
                s=s[len(key):]
                key=s
            else:
                key=key[:-1]
         
        # n=len(s)
        # res=0
        # start=0
        # end=n
        # while start<n:
        #     key=s[start:end]
        #     if numbers.get(key):
        #         res+=numbers[key]
        #         start+=len(key)
        #         end=n
        #     else:
        #         end-=1
            
        return res