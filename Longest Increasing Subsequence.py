'''For a given array with N elements, you need to find the length of the longest subsequence from the array such that all the elements of the subsequence are sorted in strictly increasing order.

Strictly Increasing Sequence is when each term in the sequence is larger than the preceding term.

For example:
[1, 2, 3, 4] is a strictly increasing array, while [2, 1, 4, 3] is not.'''

def length_of_LIS(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)
    max_length = 1

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])

    return max_length

# Example usage
if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print("Length of Longest Increasing Subsequence is:", length_of_LIS(nums))
