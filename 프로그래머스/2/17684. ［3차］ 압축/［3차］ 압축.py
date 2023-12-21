def solution(msg):
    dic = {chr(i + 64): i for i in range(1, 27)}
    def find_prefix(s):
        if s in dic:
            return s
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix not in dic:
                return prefix[:-1]
    
    def zzip(s):
        prefix = find_prefix(s)
        index = dic[prefix]
        s = s[len(prefix):]
        if not s:
            return [index]
        
        dic[prefix + s[0]] = len(dic) + 1
        return [index] + zzip(s)
    
    return zzip(msg)