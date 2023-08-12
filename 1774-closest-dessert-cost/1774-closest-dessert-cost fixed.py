from functools import reduce

def closestCost(baseCosts, toppingCosts, target):
    
    def calculate_closest(i, total):
        nonlocal res
        if i == len(toppingCosts):
            abs_cur, abs_res = abs(target-total), abs(target-res)
            if abs_cur < abs_res:
                return total
            elif abs_res < abs_cur:
                return res
            else:
                return min(res, total)
        else:
            for count in range(0, 3):
                res = calculate_closest(i+1, total + toppingCosts[i] * count)
            return res

    res=float('inf')
    for bc in baseCosts:
        res = calculate_closest(0, bc)
        
    return res


def closestCost_demo(baseCosts, toppingCosts, target):

    def find_closer(a, b):
            abs_a, abs_b = abs(target-a), abs(target-b)
            if abs_a == abs_b:
                return min(a, b)
            else:
                val = {
                    abs_a: a,
                    abs_b: b
                }
                return val[min(abs_a, abs_b)]
    
    def calculate_cost(i, total):
        if i == len(toppingCosts):
            return total
        else:
            costs = {calculate_cost(i+1, total + toppingCosts[i] * num) for num in range(3)}
            return reduce(find_closer, costs, res)

    res=float('inf')
    for bc in baseCosts:
        res = find_closer(res, calculate_cost(0, bc))
        
    return res





baseCost = [1,7]
toppingCosts = [3,4]
target = 10
print(closestCost(baseCost, toppingCosts, target))