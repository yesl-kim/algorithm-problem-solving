def solution(targets):
    targets.sort(key=lambda t: (t[1], t[0]))
    prev = 0
    shoot = 0
    for s, e in targets:
        if prev <= s:
            shoot += 1
            prev = e
    return shoot
            