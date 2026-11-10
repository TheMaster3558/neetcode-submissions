import math

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)
        return dp[amount] if dp[amount] != math.inf else -1