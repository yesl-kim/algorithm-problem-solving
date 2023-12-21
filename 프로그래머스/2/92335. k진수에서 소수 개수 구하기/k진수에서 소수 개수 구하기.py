def solution(n, k):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    def convert(n, k):
        if n < k:
            return str(n)
        몫, 나머지 = divmod(n, k)
        return convert(몫, k) + str(나머지)
    
    nums = convert(n, k).split('0')
    primes = sum(1 for x in nums if x and is_prime(int(x)))
    return primes
    
    