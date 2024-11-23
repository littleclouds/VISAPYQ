''' You are given a 'N' * 'N' maze with a rat placed at 'MAZE[0][0]'. Find and print all paths that rat can follow to reach its destination i.e. 'MAZE['N' - 1]['N' - 1]'. 
Rat can move in any direc­tion ( left, right, up and down).
Value of every cell in the 'MAZE' can either be 0 or 1. Cells with value 0 are blocked means the rat can­not enter into those cells and those with value 1 are open.
'''

def find_paths(maze, n):
    paths = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    find_paths_util(maze, 0, 0, n, "", paths, visited)
    return paths

def find_paths_util(maze, x, y, n, path, paths, visited):
    # Base case: If (x, y) is out of bounds or blocked or already visited
    if x < 0 or y < 0 or x >= n or y >= n or maze[x][y] == 0 or visited[x][y]:
        return

    # If destination is reached, add the path to the list
    if x == n - 1 and y == n - 1:
        paths.append(path)
        return

    # Mark the cell as visited
    visited[x][y] = True

    # Move in all four possible directions
    find_paths_util(maze, x + 1, y, n, path + "D", paths, visited) # Down
    find_paths_util(maze, x - 1, y, n, path + "U", paths, visited) # Up
    find_paths_util(maze, x, y + 1, n, path + "R", paths, visited) # Right
    find_paths_util(maze, x, y - 1, n, path + "L", paths, visited) # Left

    # Unmark the cell (backtrack)
    visited[x][y] = False

# Example usage
if __name__ == "__main__":
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    n = len(maze)
    paths = find_paths(maze, n)
    print("All paths:", paths)
