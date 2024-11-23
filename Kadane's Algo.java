// Given an integer array arr[]. You need to find and return the maximum sum possible from all the subarrays. 

public class MaxSubarraySum {
    // Function to find the maximum sum of a subarray
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currentSum = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }
        
        return maxSum;
    }

    // Driver code
    public static void main(String[] args) {
        MaxSubarraySum solution = new MaxSubarraySum();
        int[] nums = {2, 3, -8, 7, -1, 2, 3};
        System.out.println("Maximum subarray sum is: " + solution.maxSubArray(nums));
    }
}
