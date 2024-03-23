def solution(n):
    is_odd = lambda x: bool(x % 2)
    usage = 0
    while n:
        if is_odd(n):
            n -= 1
            usage += 1
        else:
            n = n // 2
    
    return usage