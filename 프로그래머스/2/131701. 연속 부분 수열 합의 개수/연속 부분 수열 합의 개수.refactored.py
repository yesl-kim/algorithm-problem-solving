# NOTE: sum을 매번 다시 구하지 않고 재활용할 수 있음
def solution(elements):
    res = set()
    n = len(elements)
    for i in range(n):
        _sum = 0
        for size in range(n):
            _sum += elements[(i + size) % n]
            res.add(_sum)
    return len(res)

print(solution([7, 9, 1, 1, 4]))