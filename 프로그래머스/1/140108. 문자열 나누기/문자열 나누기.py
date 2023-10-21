def solution(s):
    ans = 0
    i = 0
    while i < len(s):
        a = b = 0
        for j in range(i, len(s)):
            if s[i] == s[j]:
                a += 1
            else:
                b += 1
            if a == b:
                break
        ans += 1
        i = j+1
    return ans
                