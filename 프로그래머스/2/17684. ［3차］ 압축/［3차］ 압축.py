def solution(msg):
    dic = {chr(i + 64): i for i in range(1, 27)}
    def find_prefix(s):
        for i in range(len(s), 0, -1):
            prefix = s[:i]
            if prefix in dic:
                return prefix
    
    next_index = 27
    def zzip(s):
        nonlocal next_index
        prefix = find_prefix(s)
        index = dic[prefix]
        s = s[len(prefix):]
        if not s:
            return [index]
        
        dic[prefix + s[0]] = next_index
        next_index += 1
        return [index] + zzip(s)
    
    return zzip(msg)