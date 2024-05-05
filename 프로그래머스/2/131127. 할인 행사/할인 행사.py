from collections import defaultdict, Counter

def solution(want, number, discount):
    basket = Counter({ w: n for w, n in zip(want, number)})
    
    for x, _ in zip(discount, range(10)):
        basket[x] -= 1
        
    is_basket_empty = lambda: all(not v for v in basket.values())
        
    res = int(is_basket_empty())
    for i in range(10, len(discount)):
        basket[discount[i - 10]] += 1
        basket[discount[i]] -= 1
        res += int(is_basket_empty())
    
    return res