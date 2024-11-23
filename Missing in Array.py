''' You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). 
This array represents a permutation of the integers from 1 to n with one element missing. 
Your task is to identify and return the missing element. '''

def findMissingElement(arr, n):
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)
    return total_sum - array_sum

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 5]
    n = 5
    print("Missing element is:", findMissingElement(arr, n))
