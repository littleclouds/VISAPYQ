/* Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands. 
  Constraints:
1 ≤ n, m ≤ 500
grid[i][j] = {'0', '1'} */



class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        int totalIslands = 0;

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == '1' && !visited[row][col]) {
                    totalIslands++;
                    dfs(grid, row, col, visited);
                }
            }
        }

        return totalIslands;
    }

   private void dfs(char[][] grid, int row, int col, boolean[][] visited) {
    int rows = grid.length;
    int cols = grid[0].length;

    if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] == '0' || visited[row][col]) {
        return;
    }

    visited[row][col] = true;

    dfs(grid, row - 1, col, visited);     // Up
    dfs(grid, row + 1, col, visited);     // Down
    dfs(grid, row, col - 1, visited);     // Left
    dfs(grid, row, col + 1, visited);     // Right
    dfs(grid, row - 1, col - 1, visited); // Top-Left
    dfs(grid, row - 1, col + 1, visited); // Top-Right
    dfs(grid, row + 1, col - 1, visited); // Bottom-Left
    dfs(grid, row + 1, col + 1, visited); // Bottom-Right
}

}
