/* Given an array coins[] represent the coins of different denominations and a target value sum. You have an infinite supply of each of the valued coins{coins1, coins2, ..., coinsm}.  
Find the minimum number of coins to make the change. If not possible to make a change then return -1. */

class Solution {

    public int minCoins(int coins[], int sum) {
        // Your code goes here
        int[] dp=new int[sum+1];
        Arrays.fill(dp,Integer.MAX_VALUE);
        dp[0]=0;
        
        for(int c:coins){
            for(int i=c;i<=sum;i++){
                if(dp[i-c]!=Integer.MAX_VALUE){
                    dp[i]=Math.min(dp[i],dp[i-c]+1);
                }
            }
        }
        return dp[sum] == Integer.MAX_VALUE ? -1 : dp[sum];
        
    }
}
