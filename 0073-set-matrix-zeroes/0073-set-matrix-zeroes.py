class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h, w = len(matrix), len(matrix[0])
        def setZero(x, y):
            for i in range(h):
                matrix[i][y] = 0
            for i in range(w):
                matrix[x][i] = 0
                
        zeros = []
        for x, row in enumerate(matrix):
            for y, cell in enumerate(row):
                if cell == 0:
                    zeros.append((x, y))
        
        for x, y in zeros:
            setZero(x, y)
        