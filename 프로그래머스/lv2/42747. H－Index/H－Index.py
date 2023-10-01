

def solution(citations):
    citations.sort()
    def count(v):
        for i, x in enumerate(citations):
            if v <= x:
                return len(citations) - i
                
    
    l, r = 0, citations[-1]
    res = 0
    while l<= r:
        h = (l+r) //2
        if count(h) < h:
            r = h - 1
        else:
            res = h
            l = h + 1
    return res
    
    
            