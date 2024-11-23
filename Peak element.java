/* Given an 0-indexed array of integers arr[], find its peak element and return its index. 
An element is considered to be peak if its value is greater than or equal to the values of its adjacent elements (if they exist).
Note: The output will be "true" if the index returned by your function is correct; otherwise, it will be "false". */

public class PeakElement {
    public int findPeakElement(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[mid + 1]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    public static void main(String[] args) {
        PeakElement solution = new PeakElement();
        int[] nums = {1, 2, 3, 1};
        int peakIndex = solution.findPeakElement(nums);
        System.out.println("Peak element index: " + peakIndex);
    }
}
