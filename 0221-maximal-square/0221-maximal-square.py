class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h, w = len(matrix), len(matrix[0])
        def area(x, y):
            max_d = min(h-x, w-y)
            for d in range(1, max_d):
                for i in range(d + 1):
                    if matrix[x+i][y+d] == '0' or matrix[x+d][y+i] == '0':
                        return d ** 2
            return max_d ** 2
        
        max_area = 0
        for x in range(h):
            for y in range(w):
                if matrix[x][y] == '1':
                    _area = min(h-x, w-y)**2
                    if _area <= max_area:
                        continue
                    max_area = max(max_area, area(x, y))
        
        return max_area