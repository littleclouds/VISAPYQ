# Given an integer array arr[]. You need to find and return the maximum sum possible from all the subarrays.

def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage
if __name__ == "__main__":
    nums = [2, 3, -8, 7, -1, 2, 3]
    print("Maximum subarray sum is:", maxSubArray(nums))
