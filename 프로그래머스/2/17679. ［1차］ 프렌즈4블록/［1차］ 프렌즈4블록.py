def solution(m, n, board):
    EMPTY = '_'
    board = [list(row) for row in board]

    def find_4_blocks(x, y):
        # x, y 기준 4블록을 찾아 좌표 반환
        value = board[x][y]
        blocks = [(x, y), (x, y + 1), (x + 1, y), (x + 1, y + 1)]
        if all(0 <= nx < m and 0 <= ny < n and board[nx][ny] == value for nx, ny in blocks):
            yield from blocks
        
    def remove():
        # board 순회 -> 제거 후 제거된 블록 개수 반환 (중복처리 x)
        blocks = set()
        for i, row in enumerate(board):
            for j, block in enumerate(row):
                if block != EMPTY:
                    for x, y in find_4_blocks(i, j):
                        blocks.add((x, y))
        return blocks
    
    def relocate(blocks):
        # col 블록 재배치
        for x, y in blocks:
            board[x][y] = EMPTY

        for y in range(n):
            col = ''
            for x in range(m):
                block = board[x][y]
                if block != EMPTY or (x, y) not in blocks:
                    col += block
            
            col = EMPTY * (m - len(col)) + col # 위 -> 아래
            for i, new_block in enumerate(col):
                board[i][y] = new_block

    while True:
        removed = remove()
        if not removed:
            break
        relocate(removed)
        
    # count    
    cnt = 0
    for row in board:
        for block in row:
            if block == EMPTY:
                cnt += 1
    return cnt