/* Given an array, arr[] of distinct elements, and a number x, find if there is a pair in arr[] with a product equal to x. Return true if there exists such pair otherwise false. */



// User function Template for Java

class Solution {
    boolean isProduct(int[] arr, long x) {
        // code here
        
        if (x == 0) {
            for (int num : arr) {
                if (num == 0) return true;
            }
            return false;
        }

        // Use a HashSet to store elements we've seen
        Set<Long> set = new HashSet<>();
        
        for (int num : arr) {
            // Check if x is divisible by num to avoid floating-point issues
            if (x % num == 0) {
                long complement = x / num;

                // Check if the complement exists in the set
                if (set.contains(complement)) {
                    return true;
                }
            }
            // Add the current number to the set
            set.add((long) num);
        }
        return false; // No such pair found
    

    }
    
}
