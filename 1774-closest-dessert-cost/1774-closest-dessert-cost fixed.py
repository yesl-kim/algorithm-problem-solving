from functools import reduce
from itertools import product

def closestCost(baseCosts, toppingCosts, target):

    def closer(a, b):
        abs_a, abs_b = abs(target-a), abs(target-b)
        if abs_a < abs_b:
            return a
        elif abs_b < abs_a:
            return b
        else:
            return min(a, b)
    
    def calculate_cost(i, total):
        if i == len(toppingCosts):
            return total
        
        cost = total
        for count in range(1, 3):
            cost = closer(cost, calculate_cost(i+1, total + toppingCosts[i] * count)) # calculate 함수 안에서 조합과 비교를 같이하는게 문제
        return cost

    res=float('inf')
    for bc in baseCosts:
        res = closer(res, calculate_cost(0, bc))
    
    return res


def closestCost2(baseCosts, toppingCosts, target):

    def closer(a, b):
            abs_a, abs_b = abs(target-a), abs(target-b)
            if abs_a == abs_b:
                return min(a, b)
            else:
                val = {
                    abs_a: a,
                    abs_b: b
                }
                return val[min(abs_a, abs_b)]       
    
    def calculate(total, cb):
        idx, count = cb
        return total + toppingCosts[idx] * count

    res = float('inf')
    for bc in baseCosts:
        for cb in product(range(3), repeat=len(toppingCosts)):
            cost = reduce(calculate, enumerate(cb), bc)
            res = closer(res, cost)
    
    return res



baseCost = [1,7]
toppingCosts = [3,4]
target = 10
# baseCost = [2, 3]
# toppingCosts = [4, 5, 100]
# target = 18
print(closestCost2(baseCost, toppingCosts, target))