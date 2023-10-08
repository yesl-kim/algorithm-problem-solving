from collections import defaultdict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # grid 순회 -> 섬 라벨링, 섬 크기 계산 -> 라벨: 섬 크기 저장
        sizes = defaultdict(int)
        q = deque()
        label = 2
        h, w = len(grid), len(grid[0])
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    q.append((i, j))
                    size = 0
                    while q:
                        x, y = q.popleft()
                        if not (0<=x<h and 0<=y<w and grid[x][y] == 1):
                            continue
                        
                        size += 1
                        grid[x][y] = label
                        for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                            q.append((x+dx, y+dy))
                    sizes[label] = size
                    label += 1
        
                    
        # grid 순회 -> 0인 부분의 상하좌우 섬 크기 합 -> 최대값 계산
        max_size = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0:
                    connected = set()
                    size = 1
                    for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                        x, y = i+dx, j+dy
                        if not (0<=x<h and 0<=y<w):
                            continue
                            
                        label = grid[i+dx][j+dy]
                        if not label in connected:
                            size += sizes[label]
                        connected.add(label)
                    max_size = max(max_size, size)
        
        return max_size if max_size else h**2
                            
                
                
        # 0이 없는 경우 = 전체가 섬 하나로 연결된 경우 = 섬은 하나, 섬크기는 n**2
        