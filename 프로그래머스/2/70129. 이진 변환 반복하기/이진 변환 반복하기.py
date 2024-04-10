from collections import Counter

def solution(s):
    def recur(s):
        if s == '1':
            return 0, 0
        
        char_cnts = Counter(s)
        converted_cnt, removed_zero_cnt = recur(format(char_cnts['1'], 'b'))
        return 1 + converted_cnt,  char_cnts['0'] + removed_zero_cnt
    return list(recur(s))