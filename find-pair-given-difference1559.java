/* Given an array, arr[] and an integer x, return true if there exists a pair of elements in the array whose absolute difference is x, otherwise, return false. 
Constraints:
1<= arr.size() <=106 
1<= arr[i] <=106 
0<= x <=105 */


class Solution {
    public boolean findPair(int[] arr, int x) {
        // Sort the array
        Arrays.sort(arr);

        int i = 0;    // First pointer
        int j = 1;    // Second pointer

        x = Math.abs(x);  // Absolute value of the difference

        while (i < arr.length && j < arr.length) {
            int diff = arr[j] - arr[i];

            // If difference matches and i != j
            if (diff == x && i != j) {
                return true;
            }

            // If difference is less than x, move j forward
            if (diff < x) {
                j++;
            }
            // If difference is greater than x, move i forward
            else {
                i++;
            }

            // Ensure pointers do not overlap
            if (i == j) {
                j++;
            }
        }
        return false;
    }
}
