import math

mineral_names = ['diamond', 'iron', 'stone']
mineral_nums = {name: i for i, name in enumerate(mineral_names)}
# 피로도, t[곡괭이][광물]
t = [[1,1,1], [5,1,1], [25,5,1]]

def solution(picks, minerals):
    res = math.inf
    def dfs(ms, total = 0):
        nonlocal res
        if total > res:
            return
        if not any(picks) or not ms:
            res = min(res, total)
            return
        for p, cnt in enumerate(picks):
            if not cnt:
                continue
            picks[p] -= 1
            dfs(ms[5:], sum(t[p][mineral_nums[m]] for m in ms[:5]) + total)
            picks[p] += 1
    dfs(minerals, 0)
    return res
            