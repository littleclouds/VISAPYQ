''' Given an 0-indexed array of integers arr[], find its peak element and return its index. 
An element is considered to be peak if its value is greater than or equal to the values of its adjacent elements (if they exist).
Note: The output will be "true" if the index returned by your function is correct; otherwise, it will be "false". '''

class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    peak_index = solution.findPeakElement(nums)
    print("Peak element index:", peak_index)
