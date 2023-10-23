def solution(ingredient):
    hamburger = [1,2,3,1]
    size = len(hamburger)
    stack = []
    cnt = 0
    for i in ingredient:
        stack.append(i)
        if stack[-size:] == hamburger:
            cnt += 1
            for _ in range(size):
                stack.pop()
    return cnt
        
        