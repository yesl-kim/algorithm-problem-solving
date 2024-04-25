def solution(n):
    count_one = lambda x: format(x, 'b').count('1')
    is_valid = lambda x: count_one(n) == count_one(x)
        
    x = n + 1
    while True:
        if is_valid(x):
            return x
        x += 1