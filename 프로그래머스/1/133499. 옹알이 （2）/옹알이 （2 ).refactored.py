def solution(babbling):
    s = ['aya', 'ye', 'woo', 'ma']

    def can_speak(x: str, spoken = None) -> bool:
        return not x or any(can_speak(x[len(b):], b) for b in s if b != spoken and x.startswith(b))
    
    cnt = 0
    for b in babbling:
        if can_speak(b):
            cnt += 1

    return cnt


babbling = ["aya", "yee", "u", "maa"]
print(solution(babbling))