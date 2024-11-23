'''
You are given the weights and values of items, and you need to put these items in a knapsack of capacity capacity to achieve the maximum total value in the knapsack. 
Each item is available in only one quantity.
In other words, you are given two integer arrays val[] and wt[], which represent the values and weights associated with items, respectively. 
You are also given an integer capacity, which represents the knapsack capacity. 
Your task is to find the maximum sum of values of a subset of val[] such that the sum of the weights of the corresponding subset is less than or equal to capacity. 
You cannot break an item; you must either pick the entire item or leave it (0-1 property). '''

def knapSack(capacity, wt, val, n):
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][capacity]

# Driver code
val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50
n = len(val)
print(knapSack(capacity, wt, val, n))
