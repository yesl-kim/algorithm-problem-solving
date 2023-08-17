class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin_nums = [float('inf')]*(amount+1)
        coin_nums[0] = 0
        
        for coin in coins:
            for value in range(coin, amount+1):
                coin_nums[value] = min(coin_nums[value], coin_nums[value - coin] + 1)
        
        return coin_nums[amount] if coin_nums[amount] != float('inf') else -1