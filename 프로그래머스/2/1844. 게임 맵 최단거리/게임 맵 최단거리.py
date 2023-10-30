from collections import deque

def solution(maps):
    q = deque()
    h, w = len(maps), len(maps[0])
    q.append((0, 0))

    def path(x, y):
        for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
            xx, yy = x+dx, y+dy
            if 0 <= xx < h and 0 <= yy < w and maps[xx][yy] == 1:
                yield xx, yy

    while q:
        i, j = q.popleft()
        if i == h-1 and j == w-1:
            return maps[i][j]
        
        for x, y in path(i, j):
            maps[x][y] = maps[i][j] + 1
            q.append((x, y))

    return -1