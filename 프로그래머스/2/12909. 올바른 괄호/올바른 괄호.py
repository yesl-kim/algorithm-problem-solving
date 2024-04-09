def solution(s):
    opens = 0
    for char in s:
        if char == '(':
            opens += 1
        else:
            opens -= 1
        
        if opens < 0:
            return False
    
    return opens == 0