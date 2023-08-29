class Solution:
    def isValid(self, s: str) -> bool:
        opens=[]
        
        for x in s:
            if x == '(':
                opens.append(x)
            else:
                if not opens:
                    return False
                opens.pop()
        
        return len(opens) == 0
    
    
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(L = 0, s = ''):
            if L == n*2:
                return [s] if self.isValid(s) else []
            else:
                return generate(L+1, s+'(') + generate(L+1, s+')')

        return generate()