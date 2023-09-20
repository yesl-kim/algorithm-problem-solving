def solution(sizes):
    max_h, max_w = 0,0
    aligned = []
    for w, h in sizes:
        if w < h:
            w, h = h, w
        max_w, max_h = max(w, max_w), max(h, max_h)
    return max_h * max_w
    