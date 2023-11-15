def solution(s):
    stack = [s[0]]
    
    for x in s[1:]:
        if not stack or stack[-1] != x:
            stack.append(x)
        else:
            stack.pop()
    
    return 0 if stack else 1
        