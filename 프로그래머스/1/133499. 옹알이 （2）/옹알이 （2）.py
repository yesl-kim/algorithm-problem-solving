from itertools import product

def solution(babbling):
    s = set(['aya', 'ye', 'woo', 'ma'])
    
    cnt = 0
    for b in babbling:
        temp = b
        spoken = ''
        while temp:
            x = [x for x in s if x != spoken and temp.startswith(x)]
            if not x:
                break
            [spoken] = x
            temp = temp[len(spoken):]
        if not temp:
            cnt += 1

    return cnt