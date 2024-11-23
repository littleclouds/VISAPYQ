/*You have been given a square array 'VEC' of integers of size 'N' rows and 'N' columns. Your task is to find the minimum sum of a falling path through the square array. The number of rows and columns in the given array will be the same.

A falling path starts at any element in the first row and chooses one element from each row. The next row's choice must be in a column that is different from the previous row's column by at most one.*/

public class MinimumFallingPathSum {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int[][] dp = new int[n][n];

        // Initialize the first row of dp array
        for (int j = 0; j < n; j++) {
            dp[0][j] = matrix[0][j];
        }

        // Fill the dp array
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int minAbove = dp[i - 1][j];
                if (j > 0) {
                    minAbove = Math.min(minAbove, dp[i - 1][j - 1]);
                }
                if (j < n - 1) {
                    minAbove = Math.min(minAbove, dp[i - 1][j + 1]);
                }
                dp[i][j] = matrix[i][j] + minAbove;
            }
        }

        // Find the minimum value in the last row of dp array
        int minSum = dp[n - 1][0];
        for (int j = 1; j < n; j++) {
            minSum = Math.min(minSum, dp[n - 1][j]);
        }

        return minSum;
    }

    // Driver code
    public static void main(String[] args) {
        MinimumFallingPathSum solution = new MinimumFallingPathSum();
        int[][] matrix = {
            {2, 1, 3},
            {6, 5, 4},
            {7, 8, 9}
        };
        System.out.println("Minimum Falling Path Sum: " + solution.minFallingPathSum(matrix));
    }
}