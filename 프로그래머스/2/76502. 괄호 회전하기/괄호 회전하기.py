def is_valid_parenthesis(s):
    pairs = {'(': ')', '[': ']', '{': '}'}
    opens = []
    for x in s:
        if x in pairs:
            opens.append(x)
        elif not (opens and x == pairs[opens.pop()]):
            return False
    
    return len(opens) == 0

def solution(s):
    cnt = 0
    for i in range(len(s)):
        ns = s[i:] + s[0:i]
        if is_valid_parenthesis(ns):
            cnt += 1
    return cnt