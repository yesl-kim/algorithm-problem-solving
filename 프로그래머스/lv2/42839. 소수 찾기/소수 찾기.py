from itertools import permutations

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True

def solution(numbers):
    primes = set()
    for i in range(1, len(numbers)+1):
        for s in permutations(numbers, i):
            num = int("".join(s))
            if isPrime(num):
                primes.add(num)
    return len(primes)