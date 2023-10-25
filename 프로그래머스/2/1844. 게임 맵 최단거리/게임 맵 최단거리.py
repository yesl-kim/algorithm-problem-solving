from collections import deque

def solution(maps):
    q = deque()
    h, w = len(maps), len(maps[0])
    q.append((0,0))
    while q:
        i, j = q.popleft()
        for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
            x, y = i+dx, j+dy
            if 0 <= x < h and 0 <= y < w and maps[x][y] == 1:
                maps[x][y] = maps[i][j] + 1
                q.append((x, y))
                
    path = maps[h-1][w-1]
    return path if path > 1 else -1