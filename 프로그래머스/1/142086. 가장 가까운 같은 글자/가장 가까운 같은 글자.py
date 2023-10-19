def solution(s):
    ans = []
    for i, x in enumerate(s):
        for j, y in enumerate(s[:i][::-1]):
            if x == y:
                ans.append(j + 1)
                break
        else:
             ans.append(-1)
                
    return ans
            