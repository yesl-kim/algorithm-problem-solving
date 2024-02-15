def window(m, s):
    for i in range(0, len(s), m):
        yield s[i: i+m]

def solution(s):
    res = len(s)
    
    for m in range(1, len(s) // 2 + 1):
        zipped = ''
        target = ''
        cnt = 1
        for x in window(m, s):
            if x == target:
                cnt += 1
            else:
                zipped += f"{cnt if cnt > 1 else ''}{target}"
                target = x
                cnt = 1
        
        zipped += f"{cnt if cnt > 1 else ''}{target}"
        res = min(res, len(zipped))

    return res