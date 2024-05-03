def solution(elements):
    expanded = elements * 2
    res = set()
    for start in range(len(elements)):
        for window in range(1, len(elements)):
            res.add(sum(expanded[start:start+window]))
    res.add(sum(elements))
    return len(res)
    