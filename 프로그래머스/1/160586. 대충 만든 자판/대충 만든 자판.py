from collections import defaultdict

def solution(keymap, targets):
    count = defaultdict(lambda: float('inf'))
    for key in keymap:
        for i, char in enumerate(key):
            count[char] = min(i + 1, count[char])
    
    res = []
    for t in targets:
        c = 0
        for char in t:
            if not char in count:
                c = -1
                break
            c += count[char]
        res.append(c)
    return res