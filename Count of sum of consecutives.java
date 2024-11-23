/* Given a number N, the task is find the number of ways to represent this number as a sum of 2 or more consecutive natural numbers. */

class Solution {
    static int getCount(int N) {
        // code here
        int count = 0;
        for(int k = 2; k * (k -1) / 2 < N; k++) {
            int rem = N - (k*(k-1)) / 2;
            if(rem % k ==0) 
            count++;
        }
        
        return count;
    }
}
