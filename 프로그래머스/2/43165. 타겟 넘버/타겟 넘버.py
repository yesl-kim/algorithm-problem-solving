from collections import deque

def solution(numbers, target):
    def count(ns, t = 0):
        if not ns:
            return int(t == target)
        n = ns[0]
        return count(ns[1:], t+n) + count(ns[1:], t-n)
    
    return count(numbers)