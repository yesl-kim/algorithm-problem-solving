from typing import List
from functools import reduce

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
        pairs = ('((', '()', '))', ')(')
        def generate(n, s = ''):
            if n == 0:
                return [s] if self.isValid(s) else []
            else:
                return reduce(lambda acc, p: acc + generate(n-1, s + p), pairs, [])

        return generate(n)

s = Solution()
print(s.generateParenthesis(3))