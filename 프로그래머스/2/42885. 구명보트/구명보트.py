from collections import deque

def solution(p, limit):
    cnt = 0
    people = deque(sorted(p))
    while people:
        hi = people.pop()
        if people and hi + people[0] <= limit:
            people.popleft()
        cnt += 1
    return cnt