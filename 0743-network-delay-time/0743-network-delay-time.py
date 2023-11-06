from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프: 인접노드를 저장한 연결리스트 형태
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        Q = [(0, k)]
        dist = defaultdict(int)
        while Q:
            time, node = heappop(Q)
            if node in dist:
                continue
                
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heappush(Q, (alt, v))
        
        return max(dist.values()) if len(dist) == n else -1