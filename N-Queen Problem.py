''' The n-queens puzzle is the problem of placing n queens on a (n×n) chessboard such that no two queens can attack each other.
Given an integer n, find all distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the n-queens placement, where the solutions are a permutation of [1,2,3..n] in increasing order, here the number in the ith place denotes that the ith-column queen is placed in the row with that number
'''

from itertools import permutations
class Solution:
    def is_valid(self, permutation):
        n = len(permutation)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(i - j) == abs(permutation[i] - permutation[j]):
                    return False
        return True

    def nQueen(self, n):
        if n == 0:
            return []
        
        # Generate all permutations of [1, 2, ..., n]
        permutations_list = permutations(range(1, n + 1))
        
        # Filter valid solutions
        valid_solutions = [list(perm) for perm in permutations_list if self.is_valid(perm)]
        
        return valid_solutions
