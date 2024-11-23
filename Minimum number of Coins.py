''' Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } and a target value N.
Find the minimum number of coins and/or notes needed to make the change for Rs N. You must return the list containing the value of coins required. 
'''

#User function Template for python3

class Solution:
    def minPartition(self, N):
        # list of denominations
        denom = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        # initialize dp and dp2 arrays
        dp = [0] * (N + 1)
        dp2 = [0] * (N + 1)
        for i in range(N):
            # initialize dp with a large value
            dp[i] = 9999999999999
            # initialize dp2 with -1
            dp2[i] = -1
        # loop over the denominations
        for j in range(10):
            # loop over the values from 1 to N
            for i in range(1, N+1):
                if i >= denom[j]:
                    # update dp and dp2 arrays
                    dp[i] = min(dp[i], 1+dp[i-denom[j]])
                    dp2[i] = j
        # initialize variables
        k = N
        num = []
        i = N
        # construct the partition
        while i > 0 and N >=0:
            if dp2[i] != -1:
                num.append(denom[dp2[i]])
            N = N - denom[dp2[i]]
            i = N
        # return the partition
        return num
