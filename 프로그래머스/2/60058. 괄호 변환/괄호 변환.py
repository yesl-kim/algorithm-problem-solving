def divide(s):
    u = ''
    opens = 0
    for x in s:
        opens += 1 if x == '(' else -1
        u += x
        if not opens:
            return u, s[len(u):]
        
def is_correct(s):
    opens = 0
    for x in s:
        opens += 1 if x == '(' else -1
        if opens < 0:
            return False
    
    return opens == 0

def reverse(s):
    res = ''
    for x in s:
        res += '(' if x == ')' else ')'
    return res
    
def solution(p):
    if not p:
        return ''
    
    u, v = divide(p)
    if not is_correct(u):
        return '(' + solution(v) + ')' + reverse(u[1:-1])
    
    return u + solution(v)
    
    