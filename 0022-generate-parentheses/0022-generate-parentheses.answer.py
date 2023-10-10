class Solution:
    def generate(self, L, parenthese, sum, open, n, res):
        '''
        L: 상태트리의 레벨
        sum: ( = 1, ) = -1 일 때, parenthese의 값
        open: 여는 괄호 개수
        '''
        if L == n*2:
            if sum == 0:
                res.append(parenthese)
        else:
            if open < n:
                self.generate(L+1, parenthese + '(', sum+1, open+1, n, res)
            if 0 < sum:
                self.generate(L+1, parenthese + ')', sum-1, open, n, res)
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generate(0, '', 0, 0, n, res)
        return res