/* You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). 
This array represents a permutation of the integers from 1 to n with one element missing. 
Your task is to identify and return the missing element. */

public class MissingElement {
    // Function to find the missing element
    public int findMissingElement(int[] arr, int n) {
        int totalSum = n * (n + 1) / 2;
        int arraySum = 0;
        for (int num : arr) {
            arraySum += num;
        }
        return totalSum - arraySum;
    }

    // Driver code
    public static void main(String[] args) {
        MissingElement solution = new MissingElement();
        int[] arr = {1, 2, 3, 5};
        int n = 5;
        System.out.println("Missing element is: " + solution.findMissingElement(arr, n));
    }
}
