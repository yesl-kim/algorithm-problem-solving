from collections import Counter
from functools import reduce, lru_cache

def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True

@lru_cache
def prime_factorize(n: int) -> Counter:
    if n < 2:
        return Counter()
    
    if is_prime(n):
        return Counter({n: 1})
    
    for i in filter(is_prime, range(n)):
        share, rest = divmod(n, i)
        if not rest:
            return Counter({i: 1}) + prime_factorize(share)

def solution(arr):
    common_divisors = reduce(
        lambda a, b: a | b,
        map(prime_factorize, arr),
        Counter()
    )
    min_common_multiple = reduce(
        lambda a, b: a * b,
        (base ** exponent for base, exponent in common_divisors.items()),
        1
    )
    return min_common_multiple