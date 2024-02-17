def solution(n, info):
    SIZE = 11
    
    def find(arrows, lion_info):
        i = len(lion_info)
        if not arrows:
            return lion_info + ([0] * (SIZE - i))
        
        if i == SIZE:
            return lion_info[:-1] + [arrows]
        
        a = find(arrows, lion_info + [0])
        shoot = info[i] + 1

        if shoot > arrows:
            return a
        
        b = find(arrows - shoot, lion_info + [shoot])
        return pick(a, b)
    
    def pick(a, b):
        a_diff, b_diff = calc_diff(a), calc_diff(b)
        if a_diff > b_diff:
            return a
        if a_diff < b_diff:
            return b
        return compare(a, b)

    def calc_diff(lion_info):
        apeach, lion = 0, 0
        for i in range(SIZE):
            score = 10 - i
            a_shoot, l_shoot = info[i], lion_info[i]
            
            if not a_shoot + l_shoot:
                continue
            if a_shoot < l_shoot:
                lion += score
            else:
                apeach += score
        
        return lion - apeach
    
    def compare(a, b):
        if a == b:
            return a
        
        for i in range(SIZE - 1, -1, -1):
            if a[i] < b[i]:
                return b
            if b[i] < a[i]:
                return a
    
    res = find(n, [])
    diff = calc_diff(res)
    return res if diff > 0 else [-1]