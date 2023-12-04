class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        groups = [set() for _ in range(9)]

        def check_cell(x, y):
            cell = board[x][y]
            row = rows[x]
            col = cols[y]
            g = 3 * (x // 3) + (y // 3)
            group = groups[g]

            if cell == '.':
                return True

            if cell in row or cell in col or cell in group:
                return False
            
            row.add(cell)
            col.add(cell)
            group.add(cell)
            return True
            
        
        for i in range(9):
            for j in range(i, 9):
                valid = check_cell(i, j) if i == j else check_cell(i, j) and check_cell(j, i)
                if not valid:
                    return False
        
        return True