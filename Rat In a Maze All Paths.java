/* You are given a 'N' * 'N' maze with a rat placed at 'MAZE[0][0]'. Find and print all paths that rat can follow to reach its destination i.e. 'MAZE['N' - 1]['N' - 1]'. 
Rat can move in any direc­tion ( left, right, up and down).
Value of every cell in the 'MAZE' can either be 0 or 1. Cells with value 0 are blocked means the rat can­not enter into those cells and those with value 1 are open.
*/

import java.util.ArrayList;
import java.util.List;

public class RatInMaze {
    public List<String> findPaths(int[][] maze, int n) {
        List<String> paths = new ArrayList<>();
        boolean[][] visited = new boolean[n][n];
        findPathsUtil(maze, 0, 0, n, "", paths, visited);
        return paths;
    }

    private void findPathsUtil(int[][] maze, int x, int y, int n, String path, List<String> paths, boolean[][] visited) {
        // Base case: If (x, y) is out of bounds or blocked or already visited
        if (x < 0 || y < 0 || x >= n || y >= n || maze[x][y] == 0 || visited[x][y]) {
            return;
        }

        // If destination is reached, add the path to the list
        if (x == n - 1 && y == n - 1) {
            paths.add(path);
            return;
        }

        // Mark the cell as visited
        visited[x][y] = true;

        // Move in all four possible directions
        findPathsUtil(maze, x + 1, y, n, path + "D", paths, visited); // Down
        findPathsUtil(maze, x - 1, y, n, path + "U", paths, visited); // Up
        findPathsUtil(maze, x, y + 1, n, path + "R", paths, visited); // Right
        findPathsUtil(maze, x, y - 1, n, path + "L", paths, visited); // Left

        // Unmark the cell (backtrack)
        visited[x][y] = false;
    }

    // Driver code
    public static void main(String[] args) {
        RatInMaze solution = new RatInMaze();
        int[][] maze = {
            {1, 0, 0, 0},
            {1, 1, 0, 1},
            {0, 1, 0, 0},
            {1, 1, 1, 1}
        };
        int n = maze.length;
        List<String> paths = solution.findPaths(maze, n);
        System.out.println("All paths: " + paths);
    }
}
