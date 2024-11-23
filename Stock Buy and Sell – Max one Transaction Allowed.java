/* Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. 
Here one transaction means 1 buy + 1 Sell. 
If it is not possible to make a profit then return 0. */

class Solution {
    public int maximumProfit(int prices[]) {
        // Code here
        int ans = 0;
        int st = 0;
        
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < prices[st]) {
                st = i;
            }
            else {
                ans = Math.max(ans, prices[i] - prices[st]);
            }
        }
        return ans;
    }
}
