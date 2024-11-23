''' Given a strictly sorted 2D array matrix and a number x. Find whether element x is present in the matrix or not.
Note: In a strictly sorted matrix, each row is sorted in itself and the first element of the ith row (i!=0) is greater than the last element of the (i-1)th row.
'''
#Back-end complete function Template for Python 3


class Solution:
    #Function to search a given number in a strictly sorted matrix.
    def searchMatrix(self, mat, x):
        n = len(mat)  # Number of rows
        m = len(mat[0])  # Number of columns

        left, right = 0, n * m - 1

        # Perform binary search
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = mat[mid // m][mid % m]  # Convert 1D index to 2D

            if mid_value == x:
                return 1  # Found the target
            elif mid_value < x:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half

        return 0  # Element not found
