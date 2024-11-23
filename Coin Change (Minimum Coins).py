# Given an array coins[] represent the coins of different denominations and a target value sum. You have an infinite supply of each of the valued coins{coins1, coins2, ..., coinsm}.  
# Find the minimum number of coins to make the change. If not possible to make a change then return -1.

#User function Template for python3
class Solution:
    def minCoins(self, coins, su):
        # Remove zero-valued coins
        coins = [c for c in coins if c > 0]
        if su == 0:
            return 0
        if not coins:
            return -1

        # Initialize DP array
        dp = [float('inf')] * (su + 1)
        dp[0] = 0  # Base case: 0 coins needed to make sum 0

        # Update DP array for each coin
        for coin in coins:
            for x in range(coin, su + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        # If dp[su] is still infinity, the sum is not possible
        return -1 if dp[su] == float('inf') else dp[su]


        
        
