''' 
Given an unsorted array arr containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. 
You need to return the 1-based indices of the leftmost and rightmost elements of this subarray.
'''

def find_subarray(arr, target):
    current_sum = 0
    sum_map = {0: 0}  # To handle the case when subarray starts from index 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum - target in sum_map:
            return sum_map[current_sum - target] + 1, i + 1  # 1-based indices

        sum_map[current_sum] = i + 1

    return -1, -1  # If no subarray is found

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 7, 5]
    target = 12
    result = find_subarray(arr, target)
    print("Subarray indices:", result)
