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
            cost = closer(cost, calculate_cost(i+1, total + toppingCosts[i] * count))
        return cost

    res=float('inf')
    for bc in baseCosts:
        res = closer(res, calculate_cost(0, bc))
    
    return res


# 1. calculate_closest의 toppingCosts 참조 제거 -> every_costs
# 2. product 활용
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

    # def calculate_closest(total, costs):
    #     if not costs:
    #         return total
        
    #     costs = [calculate_closest(total + count * costs[0], costs[1:]) for count in range(3)]
    #     print(costs)
    #     return costs
    
    def every_costs(total, topping_costs):
        return [reduce(calculate, enumerate(cb), total) for cb in product(range(3), repeat=len(topping_costs))]
            
        # if not costs:
        #     return [total]
        
        # costss = [every_costs(total + count * costs[0], costs[1:]) for count in range(3)] # 3중 for문
        # return costss[0] + costss[1] + costss[2]
    
    def calculate(total, topping):
        idx, count = topping
        return total + toppingCosts[idx] * count


    res = float('inf')
    for bc in baseCosts:
        res = every_costs(bc, toppingCosts)
        print(res)





baseCost = [1,7]
toppingCosts = [3,4]
target = 10
# baseCost = [2, 3]
# toppingCosts = [4, 5, 100]
# target = 18
print(closestCost2(baseCost, toppingCosts, target))