class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h, w = len(matrix), len(matrix[0])
        visited = [[False] * w for _ in range(h)]
        ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def next_step(x, y, d):
            dl = len(ds)
            for i in range(d, d + dl):
                next_d = i % dl
                dx, dy = ds[next_d]
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w:
                    yield nx, ny, next_d


        def spiral(x = 0, y = 0, d = 0):
            visited[x][y] = True
            cur = matrix[x][y]
            yield cur
            
            for nx, ny, next_d in next_step(x, y, d):
                if not visited[nx][ny]:
                    yield from spiral(nx, ny, next_d)
                    return
        
        return list(spiral())