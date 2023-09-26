from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = deque()
        for x, row in enumerate(grid):
            for y, orange in enumerate(row):
                if orange == 2:
                    rotten.append((0,x,y))
                if orange == 1:
                    fresh += 1
        m = 0
        w, h = len(grid), len(grid[0])
        while rotten:
            m, x, y = rotten.popleft()
            for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                xx, yy = x+dx, y+dy
                if 0<=xx<w and 0<=yy<h and grid[xx][yy] == 1:
                    grid[xx][yy] = 2
                    fresh -= 1
                    rotten.append((m+1, xx, yy))
        
        return m if fresh == 0 else -1