def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)


def find(arr, k):
    if not arr:
        return []
    
    m = factorial(len(arr) - 1)
    i, rest = divmod(k, m)

    if rest == 0:
        return [arr.pop(i-1)] + find(arr, m)
    
    return [arr.pop(i)] + find(arr, rest)


def solution(n, k):
    ns = list(range(1, n+1))
    return find(ns, k)