/* Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } and a target value N.
Find the minimum number of coins and/or notes needed to make the change for Rs N. You must return the list containing the value of coins required. */



// User function Template for Java

class Solution{
    static List<Integer> minPartition(int N)
    {
       int[] currency = {2000,500,200,100,50,20,10,5,2,1};
       ArrayList<Integer> ans = new ArrayList<Integer>();
        
        int notes = 0, i =0;
        
        while(N > 0){
            notes = N/currency[i];
            while(notes > 0){
                
                ans.add(currency[i]);
                notes--;
                
            }
            N = N%currency[i];
            i++;
        }
        
        return ans;
    }
}
