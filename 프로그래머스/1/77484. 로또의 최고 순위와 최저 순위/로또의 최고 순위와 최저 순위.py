def solution(lottos, win_nums):
    scores = [6, 6, 5, 4, 3, 2, 1]
    win_nums = set(win_nums)
    
    unknown, matched = 0, 0
    for x in lottos:
        if x == 0:
            unknown += 1
        elif x in win_nums:
            matched += 1
    
    return [scores[unknown + matched], scores[matched]]