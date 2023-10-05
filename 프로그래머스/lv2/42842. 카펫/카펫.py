def solution(brown, yellow):
    cases = [(yellow // v, v) for v in range(1, (yellow+1) // 2 +1) if yellow % v == 0]
    for w, h in cases:
        if (w+h)*2+4 == brown:
            return [w+2, h+2]