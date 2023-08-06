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
        parentheses = ['(', ')']
        res = []
        
        def generate(L = 0, s = ''):
            if L == n*2:
                if self.isValid(s):
                    res.append(s)
            else:
                for i in range(2):
                    generate(L+1, s+parentheses[i])
        
        generate()
        return res