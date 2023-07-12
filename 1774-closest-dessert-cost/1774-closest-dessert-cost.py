
class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        global res
        res=float('inf')
        def dfs(L,sum):
            global res
            a,b=abs(target-res),abs(target-sum)
            if res<sum and a<b: return
            if L==len(toppingCosts):
                if a>b:
                    res=sum
                elif a==b:
                    res=min(res,sum)
            else:
                for n in range(3):
                    dfs(L+1,sum+(n*toppingCosts[L]))

        for bc in baseCosts:
            dfs(0,bc)
        return res
        