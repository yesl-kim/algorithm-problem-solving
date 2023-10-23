from collections import Counter
from functools import reduce
from operator import mul

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def prime_factorize(n: int) -> Counter:
    if isPrime(n):
        return Counter({n: 1})
    
    for i in filter(isPrime, range(n)):
        share, rest = divmod(n, i)
        if not rest:
            return Counter({i: 1}) + prime_factorize(share)


def count_divisor(n):
    if n == 1:
        return 1
    primes = prime_factorize(n)
    return reduce(mul, (b+1 for b in primes.values()))


def solution(number, limit, power):
    answer = 0
    for n in range(1, number+1):
        cnt = count_divisor(n)
        weapon = power if limit < cnt else cnt
        answer += weapon
    return answer