class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,profit=100000,0
        for p in prices:
            if buy>p:
                buy=p
            else:
                profit=max(p-buy,profit)
        return profit
        