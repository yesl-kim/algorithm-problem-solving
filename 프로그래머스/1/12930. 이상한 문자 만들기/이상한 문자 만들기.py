def solution(s):
    i = 0
    ns = ''
    for char in s:
        if char == ' ':
            i = 0
            ns += char
            continue
        
        if i % 2 == 0:
            ns += char.upper()
        else:
            ns += char.lower()
        i += 1
    return ns