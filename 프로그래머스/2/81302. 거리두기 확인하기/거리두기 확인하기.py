from collections import deque

def solution(places):
    def distance(t1, t2):
        x1, y1 = t1
        x2, y2 = t2
        return abs(x1 - x2) + abs(y1 - y2)
    
    def adj(x, y):
        h, w = 5, 5
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                yield nx, ny
    
    def check(x, y, place):
        q = deque(list(adj(x, y)))
        visited = [[0] * 5 for _ in range(5)]
        visited[x][y] = 1
        while q:
            nx, ny = q.popleft()
            # 방문확인
            if visited[nx][ny]:
                continue
            
            if distance((x, y), (nx, ny)) > 2:
                continue
            
            v = place[nx][ny] 
            if v == 'P':
                return False
            
            if v == 'X':
                continue
            
            if v == 'O':
                for np in adj(nx, ny):
                  q.append(np)
            
            # 방문처리
            visited[nx][ny] = 1
        return True
            
        
    answer = []
    for place in places:
        ps = []
        for x, row in enumerate(place):
            for y, cell in enumerate(row):
                if cell == 'P':
                    ps.append((x, y))
        answer.append(int(all((check(x, y, place) for x, y in ps))))
                
    return answer