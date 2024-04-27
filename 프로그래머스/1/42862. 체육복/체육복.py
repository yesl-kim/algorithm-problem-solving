def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for i in range(1, n + 1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
    
    absence = 0
    for x in lost:
        left, right = x - 1, x + 1
        if left in reserve:
            reserve.remove(left)
        elif right in reserve:
            reserve.remove(right)
        else:
            absence += 1
    return n - absence