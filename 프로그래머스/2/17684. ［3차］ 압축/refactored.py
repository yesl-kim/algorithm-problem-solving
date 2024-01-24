def solution(msg):
    init_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = {char: i + 1 for i, char in enumerate(init_chars)}
    
    def find_prefix(x):
        for prefix in sorted(d, key=len, reverse=True):
            if x.startswith(prefix):
                return prefix
        return None
    
    def zip(s):
        if not s:
            return []
        
        prefix = find_prefix(s)
        if not prefix:
            return []
        
        idx = d[prefix]
        ns = s[len(prefix):]
        if ns:
            new_prefix = prefix + ns[0]
            d[new_prefix] = len(d) + 1

        yield idx
        yield from zip(ns)
    
    return list(zip(msg))
    
msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))