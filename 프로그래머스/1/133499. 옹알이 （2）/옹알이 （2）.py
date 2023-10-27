def solution(babbling):
    s = ['aya', 'ye', 'woo', 'ma']
    def can_speak(babbling: str, spoken = '') -> bool:
        if not babbling:
            return True
        for x in s:
            if x != spoken and babbling.startswith(x):
                return can_speak(babbling[len(x):], x)
        return False
    
    cnt = 0
    for b in babbling:
        if can_speak(b):
            cnt += 1

    return cnt


babbling = ["aya", "yee", "u", "maa"]
print(solution(babbling))