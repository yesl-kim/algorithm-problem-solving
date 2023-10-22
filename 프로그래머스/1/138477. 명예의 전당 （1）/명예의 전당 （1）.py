from heapq import heappop, heappush, heapify

def solution(k, score):
    res = []
    heap = []
    for s in score:
        heappush(heap, s)
        if k < len(heap):
            heappop(heap)
        res.append(heap[0])
    return res