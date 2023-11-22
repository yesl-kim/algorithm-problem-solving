from collections import deque
from heapq import heapify, heappop, heappush

def solution(priorities, location):
    q = deque(list(enumerate(priorities)))
    priorities = [-p for p in priorities]
    heapify(priorities)

    cnt = 0
    while q:
        i, v = q.popleft()
        largest = heappop(priorities) * -1
        if v == largest:
            cnt += 1
            if i == location:
                return cnt
        elif v < largest:
            q.append((i, v))
            heappush(priorities, -largest)
        
    return cnt