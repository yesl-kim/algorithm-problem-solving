class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def find(x):
            if 3 ** x == n:
                return True
            elif n < 3 ** x:
                return False
            else:
                return find(x+1)
        
        return find(0)