from collections import Counter

def solution(s):
    def recur(s):
        if s == '1':
            return 0, 0
        
        char_cnts = Counter(s)
        yield 1, char_cnts['0']
        yield from recur(format(char_cnts['1'], 'b'))
    
    return [sum(x) for x in zip(*recur(s))]

s = "110010101001"
s = "01110"

print(solution(s))