'''Given a 2D matrix mat[][], where every row and column is sorted in increasing order, and a number x the task is to find whether element x is present in the matrix or not.'''

#User function Template for python3
class Solution:
    def matSearch(self,mat, x):
        check=False
        # Complete this function
        for i in range(0,len(matrix)):
            if matrix[i][0]<=x and matrix[i][-1]>=x:
                for j in range(0,len(matrix[i])):
                    if matrix[i][j]==x:
                        check=True
                        break
               
        return check
