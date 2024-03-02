def solution(queue1, queue2):
    target, rest = divmod(sum(queue1) + sum(queue2), 2)
    if rest:
        return -1
    
    cnt = 0
    q = queue2 + queue1 + queue2
    size = len(queue1)
    total = sum(queue1)
    left, right = size, size * 2
    while left <= right and 0 <= left and right < size * 3:
        if total == target:
            return cnt
        
        if total < target:
            total += q[right]
            right += 1
        else:
            total -= q[left]
            left += 1
        
        cnt += 1
    
    return cnt if total == target else -1