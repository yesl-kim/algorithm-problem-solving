# https://docs.google.com/document/d/1N_dDKC1XXgyVkj3qOeKqK-yTusFKiK4kWFShfRWARqw/edit

from typing import List

def solution(h:int, w:int, positions: List[List[int]]) -> List[int]:
    def side_lands(x, y):
        for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
            xx, yy = x+dx, y+dy
            if 0<=xx<h and 0<=yy<w and 0 < grid[xx][yy]:
                yield xx, yy
    
    def connect(x, y, label):
        if grid[x][y] == label:
            return
        
        grid[x][y] = label
        for xx, yy in side_lands(x, y):
            connect(xx, yy, label)
            
    res = []
    cnt = 0
    grid = [[0]*w for _ in range(h)]
    for i, (r, c) in enumerate(positions):
        lands = set()
        for x, y in side_lands(r, c):
            lands.add(grid[x][y])
        
        if lands:
            cnt -= (len(lands) - 1)
            connect(r, c, i + 1)
        else:
            cnt += 1
            grid[r][c] = i + 1
        
        res.append(cnt)
    return res

m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1], [1, 1]]
print('=>', solution(m, n, positions))