from functools import reduce

def closestCost(baseCosts, toppingCosts, target):
    
    def calculate_closest(i, total):
        # nonlocal res # <-- 얘를 빼
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


def closestCost(baseCosts, toppingCosts, target):

    def find_closer(a, b):
        abs_a, abs_b = abs(target-a), abs(target-b)
        if abs_a < abs_b:
            return a
        elif abs_b < abs_a:
            return b
        else:
            return min(a, b)
    
    def calculate_closest(i, total):
        if i == len(toppingCosts):
            return total
        
        cost = total
        for count in range(1, 3):
            next_cost = calculate_closest(i+1, total + (count * toppingCosts[i]))
            abs_cur, abs_next = abs(target-cost), abs(target-next_cost)
            if abs_cur == abs_next:
                return min(cost, next_cost)
            else:
                val = {
                    abs_cur: cost,
                    abs_next: next_cost
                }
                return val[min(abs_cur, abs_next)]
        return cost

    res=float('inf')
    for bc in baseCosts:
        res = find_closer(res, calculate_closest(0, bc))
        
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
            res.add(total)
            return
        
        for count in range(3):
            calculate_cost(i+1, total + toppingCosts[i] * count)

    res=set()
    for bc in baseCosts:
        calculate_cost(0, bc)

    return reduce(find_closer, res, float('inf'))





# baseCost = [1,7]
# toppingCosts = [3,4]
# target = 10
baseCost = [2, 3]
toppingCosts = [4, 5, 100]
target = 18
print(closestCost_demo(baseCost, toppingCosts, target))