from collections import defaultdict
from heapq import heappop, heappush

def solution(N, road, K):
    adj = defaultdict(list)
    for a, b, time in road:
        adj[a].append((b, time))
        adj[b].append((a, time))
    
    q = [(0, 1, None)]
    valid = set()
    while q:
        time, node, prev = heappop(q)
        if time > K:
            continue
        if node in valid:
            continue
            
        valid.add(node)
        for b, t in adj[node]:
            if b != prev:
                heappush(q, (time + t, b, node))
    
    print(valid)
    return len(valid)