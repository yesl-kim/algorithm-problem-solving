def solution(s):
    return " ".join((x.capitalize() for x in s.lower().split(" ")))