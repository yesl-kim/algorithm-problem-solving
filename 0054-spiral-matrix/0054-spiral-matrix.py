class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h, w = len(matrix), len(matrix[0])
        visited = [[False] * w for _ in range(h)]
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        res = []

        def spiral(x, y, d = 0):
            visited[x][y] = True
            res.append(matrix[x][y])
            for i in range(d, d + 4):
                next_dir = i % 4
                dx, dy = directions[next_dir]
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                    return spiral(nx, ny, next_dir)
        
        spiral(0, 0)
        return res