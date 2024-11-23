''' Given a number N, the task is find the number of ways to represent this number as a sum of 2 or 
more consecutive natural numbers.
'''

class Solution:
    def getCount(self, N):
        count = 0
        k = 2
        
        # Loop over possible values of k (number of terms in the sequence)
        while (k * (k - 1)) // 2 < N:
            # Calculate the numerator
            numerator = N - (k * (k - 1)) // 2
            
            # Check if the numerator is divisible by k
            if numerator % k == 0:
                x = numerator // k
                if x > 0:
                    count += 1
            k += 1
        
        return count
    
