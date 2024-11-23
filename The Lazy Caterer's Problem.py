'''
Given an integer n, denoting the number of cuts that can be made on a pancake, find the maximum number of pieces that can be formed by making n cuts.
NOTE: Cuts can't be horizontal.
'''

class Solution:
    def maximum_Cuts(self, n):
        return 1 + n * (n + 1)//2 
