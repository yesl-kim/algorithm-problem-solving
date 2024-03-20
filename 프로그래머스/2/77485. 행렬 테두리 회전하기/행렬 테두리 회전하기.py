def solution(rows, cols, queries):
    matrix = [[0] + list(map(lambda i: r * cols + i, range(1, cols + 1))) for r in range(rows)]
    matrix.insert(0, [0] * (cols + 1))
    
    def border(x1, y1, x2, y2):
        values = [] # (x, y, value)[]
        get_value = lambda x, y: (x, y, matrix[x][y])
        x, y = x1, y1
        while y < y2:
            values.append(get_value(x, y))
            y += 1
        while x < x2:
            values.append(get_value(x, y))
            x += 1
        while y > y1:
            values.append(get_value(x, y))
            y -= 1
        while x > x1:
            values.append(get_value(x, y))
            x -= 1
        return values
    
    res = []
    for q in queries:
        border_values = border(*q)
        new_values = [border_values[-1]] + border_values
        min_value = float('inf')
        for i, (x, y, v) in enumerate(border_values):
            min_value = min(min_value, v)
            matrix[x][y] = new_values[i][2]
        res.append(min_value)
        
    return res