def closestCost(baseCosts, toppingCosts, target):
    res=float('inf')
        
    def make(i, total, acc):
        print(i, total, acc)

        if i == len(toppingCosts):
            abs_cur, abs_acc = abs(target - total), abs(target - acc)
            if abs_cur < abs_acc:
                return total
            elif abs_cur > abs_acc:
                return acc
            else:
                return min(total, acc)
        else:
            for count in range(3):
                acc = make(i+1, total + (count * toppingCosts[i]), acc)
            return acc

    for bc in baseCosts:
        res = make(0, bc, res)
        
    return res


baseCost = [1,7]
toppingCosts = [3,4]
target = 10
print(closestCost(baseCost, toppingCosts, target))