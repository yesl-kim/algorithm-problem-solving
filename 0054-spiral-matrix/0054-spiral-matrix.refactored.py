class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h, w = len(matrix), len(matrix[0])
        visited = [[False] * w for _ in range(h)]

        def next_step(x, y, d):
            directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
            dl = len(directions)
            for i in range(d, d + dl):
                next_dir = i % dl
                dx, dy = directions[next_dir]
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w:
                    yield nx, ny, next_dir


        def spiral(x = 0, y = 0, dir = 0):
            visited[x][y] = True
            cur = matrix[x][y]
            yield cur
            
            for nx, ny, next_dir in next_step(x, y, dir):
                if not visited[nx][ny]:
                    yield from spiral(nx, ny, next_dir)
                    return
        
        return list(spiral())