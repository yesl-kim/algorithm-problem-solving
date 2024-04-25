def solution(n):
    cnt = 0
    for start in range(1, n + 1):
        x = 0
        for i in range(start, n + 1):
            if x < n:
                x += i
            else:
                break
        if x == n:
            cnt += 1
    
    return cnt