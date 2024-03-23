def solution(n):
    usage = 0
    while n:
        usage += n % 2
        n = n // 2
    
    return usage