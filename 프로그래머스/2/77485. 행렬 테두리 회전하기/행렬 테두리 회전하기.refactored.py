from collections import deque

def solution(rows, cols, queries):
    matrix = [[0] * (cols + 1)]
    matrix += [[0] + [r * cols + i for i in range(1, cols + 1)] for r in range(rows)]
    
    get_value = lambda c: matrix[c[0]][c[1]]
    def border(x1, y1, x2, y2):
        x, y = x1, y1
        while y < y2:
            yield x, y
            y += 1
        while x < x2:
            yield x, y
            x += 1
        while y > y1:
            yield x, y
            y -= 1
        while x > x1:
            yield x, y
            x -= 1
    
    res = []
    for q in queries:
        min_value = float('inf')

        border_coordinates = list(border(*q))
        values = deque(map(get_value, border_coordinates))
        values.rotate(1)

        for (x, y), v in zip(border_coordinates, values):
            min_value = min(min_value, v)
            matrix[x][y] = v
        
        res.append(min_value)
    return res