'''
Given a sequence of moves for a robot. Check if the sequence is circular or not.

A sequence of moves is circular if the first and last positions of the robot are the same. A move can be one of the following :
    G - Go one unit
    L - Turn left
    R - Turn right
You don't need to read input or print anything. Your task is to complete the function isCircular() which takes the string path as input and returns "Circular" if the path is circular else returns "Not Circular".

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |S| ≤ 105
'''

#User function Template for python3
class Solution:
    def isCircular(self, path):
        # Directions represent North, East, South, and West
        # North -> (dx, dy) = (0, 1)
        # East -> (dx, dy) = (1, 0)
        # South -> (dx, dy) = (0, -1)
        # West -> (dx, dy) = (-1, 0)
        
        # Starting at (0, 0), facing North (direction = 0)
        x, y = 0, 0
        direction = 0  # 0 -> North, 1 -> East, 2 -> South, 3 -> West
        
        for move in path:
            if move == 'G':
                # Move forward in the current direction
                if direction == 0:  # North
                    y += 1
                elif direction == 1:  # East
                    x += 1
                elif direction == 2:  # South
                    y -= 1
                elif direction == 3:  # West
                    x -= 1
            elif move == 'L':
                # Turn left (counter-clockwise)
                direction = (direction + 3) % 4  # Equivalent to direction - 1
            elif move == 'R':
                # Turn right (clockwise)
                direction = (direction + 1) % 4  # Equivalent to direction + 1
        
        # If we are back at the origin, it's circular
        if x == 0 and y == 0:
            return "Circular"
        else:
            return "Not Circular"

        # code here
