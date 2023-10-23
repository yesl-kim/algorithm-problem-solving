def solution(k, m, score):
    res = 0
    for s in sorted(score, reverse=True)[m-1::m]:
        res += s * m
    return res