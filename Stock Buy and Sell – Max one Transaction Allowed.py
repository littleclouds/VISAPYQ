''' Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. 
If it is not possible to make a profit then return 0.
'''

  class Solution:
    def maximumProfit(self, prices):
        # code here
        n = len(prices)
        sell = float('-inf')
        ans = float('-inf')
        for i in range(n-1, -1, -1):
            sell = max(sell, prices[i])
            ans = max(ans, sell - prices[i])
        return ans
