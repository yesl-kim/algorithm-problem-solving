def solution(n, wires):
    maps = [[False] * (n + 1) for _ in range(n + 1)] # 1 indexed
    for x, y in wires:
        maps[x][y] = True
        maps[y][x] = True
    
    def count(x):
        res = 1
        for y, connected in enumerate(maps[x]):
            if not connected:
                continue
            maps[x][y] = False
            maps[y][x] = False
            res += count(y)
            maps[x][y] = True
            maps[y][x] = True
        return res
        # return 1 + sum(count(y) for y, connected in enumerate(maps[x]) if connected)
    
    res = float('inf')
    for x, y in wires:
        maps[x][y] = False
        maps[y][x] = False
        res = min(res, abs(count(x) - count(y)))
        maps[x][y] = True
        maps[y][x] = True
    
    return res
        
        