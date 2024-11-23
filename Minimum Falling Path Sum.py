'''You have been given a square array 'VEC' of integers of size 'N' rows and 'N' columns. Your task is to find the minimum sum of a falling path through the square array. The number of rows and columns in the given array will be the same.

A falling path starts at any element in the first row and chooses one element from each row. The next row's choice must be in a column that is different from the previous row's column by at most one.'''

def min_falling_path_sum(matrix):
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first row of dp array
    for j in range(n):
        dp[0][j] = matrix[0][j]

    # Fill the dp array
    for i in range(1, n):
        for j in range(n):
            min_above = dp[i - 1][j]
            if j > 0:
                min_above = min(min_above, dp[i - 1][j - 1])
            if j < n - 1:
                min_above = min(min_above, dp[i - 1][j + 1])
            dp[i][j] = matrix[i][j] + min_above

    # Find the minimum value in the last row of dp array
    min_sum = dp[n - 1][0]
    for j in range(1, n):
        min_sum = min(min_sum, dp[n - 1][j])

    return min_sum

# Example usage
if __name__ == "__main__":
    matrix = [
        [2, 1, 3],
        [6, 5, 4],
        [7, 8, 9]
    ]
    print("Minimum Falling Path Sum:", min_falling_path_sum(matrix))
