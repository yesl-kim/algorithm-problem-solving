from typing import List

def solution(s: str) -> List[str]:
    substrings = set()
    last_index = {char: i for i, char in enumerate(s)}

    start, end = 0, last_index[s[0]]
    for i, char in enumerate(s):
        if end < i:
            substrings.add(s[start: end + 1])
            start, end = i, last_index[char]
        else:
            end = max(end, last_index[char])

    substrings.add(s[start: end + 1])
    return substrings


s = "abmowodfsxadejihgepczpc"
print(solution(s))