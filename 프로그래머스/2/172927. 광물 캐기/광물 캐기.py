import math

mineral_names = ['diamond', 'iron', 'stone']
mineral_nums = {name: i for i, name in enumerate(mineral_names)}
# 피로도, t[곡괭이][광물]
t = [[1,1,1], [5,1,1], [25,5,1]]

def solution(picks, minerals):
    def dfs(ms):
        if not ms or not any(picks):
            yield 0
        for p, cnt in enumerate(picks):
            if not cnt:
                continue
            picks[p] -= 1
            yield sum(t[p][mineral_nums[m]] for m in ms[:5]) + min(dfs(ms[5:]))
            picks[p] += 1
        
    
    return min(dfs(minerals))
            