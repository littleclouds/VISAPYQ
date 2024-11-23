'''
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.
Constraints:
1 ≤ n, m ≤ 500
grid[i][j] = {'0', '1'}
'''

#User function Template for python3

class Solution:
    def numIslands(self, grid):
        # code here
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]

        # Function to check if the given coordinates are valid or not.
        def isValid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        # Depth First Search to explore the connected components (iterative).
        def dfs(grid, x, y):
            stack = [(x, y)]
            while stack:
                curr_x, curr_y = stack.pop()
                visited[curr_x][curr_y] = 1
                # Check all 8 possible directions
                for i in [[-1, -1], [1, 1], [1, 0], [0, 1], [1, -1], [-1, 1],
                          [-1, 0], [0, -1]]:
                    new_x, new_y = curr_x + i[0], curr_y + i[1]
                    if isValid(new_x, new_y) and not visited[new_x][new_y]:
                        if grid[new_x][new_y] == 1:
                            stack.append((new_x, new_y))

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    dfs(grid, i, j)
                    count += 1

        return count
