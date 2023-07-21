from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q=deque()
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        m,n,cnt=len(grid),len(grid[0]),0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    cnt+=1
                    grid[i][j]='0'
                    q.append((i,j))
                    while q:
                        x,y=q.popleft()
                        for d in range(4):
                            xx,yy=x+dx[d],y+dy[d]
                            if 0<=xx<m and 0<=yy<n and grid[xx][yy]=="1":
                                grid[xx][yy]='0'
                                q.append((xx,yy))
        return cnt