def solution(s):
    length = len(s)
    return (length == 4 or length == 6) and all(w.isdigit() for w in s)