''' Given an array, arr[] of distinct elements, and a number x, find if there is a pair in arr[] with a product equal to x. 
Return true if there exists such pair otherwise false.'''

#User function Template for python3


class Solution:
    #Function to check if there are two numbers in the array whose product equals x.
    def isProduct(self, arr, x):
        k = set(arr)
        #iterating over array elements.
        for i in arr:
            if i == 0:
                continue
            elif x / i in k:
                return True
        return False
