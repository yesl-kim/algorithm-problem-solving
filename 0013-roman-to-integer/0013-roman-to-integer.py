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
        keys=list(numbers.keys())
        i=len(keys)-1
        while s:
            k=keys[i]
            if s.startswith(k):
                res+=numbers[k]
                s=s[len(k):]
            else:
                i-=1
        # 근데 이렇게 하면 o(nm)의 시간복잡도?
        # n=s의 길이, m=numbers의 길이
        # III일 때 오히려 시간이 오래걸릴 것 같은데
        
        return res