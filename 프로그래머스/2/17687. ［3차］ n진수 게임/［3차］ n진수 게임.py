def solution(n, t, m, p):
    def convert(n, base):
        T = "0123456789ABCDEF"
        q, r = divmod(n, base)

        return convert(q, base) + T[r] if q else T[r]
        
    words = []
    for i in range(10**7):
        words += list(convert(i, n))
        if len(words) >= m * t:
            break
    
    # i = 1
    # while len(words) < m * t:
    #     words += list(convert(i, n))
    #     i += 1
    
    
    speak = words[p - 1::m][:t]
    return "".join(speak)