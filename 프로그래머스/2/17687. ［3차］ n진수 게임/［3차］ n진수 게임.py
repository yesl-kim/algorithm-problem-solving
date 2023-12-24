def solution(n, t, m, p):
    def convert(n, base):
        T = "0123456789ABCDEF"
        q, r = divmod(n, base)

        return convert(q, base) + T[r] if q else T[r]
        
    words = []
    dic = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    for i in range(10**7):
        x = convert(i, n)
        ws = [dic.get(x, x)] if i < n else list(x)
        words += ws
        if len(words) >= m * t + p:
            break
    
    
    speak = words[p - 1::m][:t]
    return "".join(speak)