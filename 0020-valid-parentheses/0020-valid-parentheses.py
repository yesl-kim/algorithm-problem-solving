class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match={
            '(':')',
            '{':'}',
            '[':']'
        }
        for x in s:
            if x in match:
                stack.append(x)
            elif not stack or match[stack.pop()]!=x:
                return False
        
        return len(stack)==0