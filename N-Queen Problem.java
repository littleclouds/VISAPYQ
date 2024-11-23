/* The n-queens puzzle is the problem of placing n queens on a (n×n) chessboard such that no two queens can attack each other.
Given an integer n, find all distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the n-queens placement, where the solutions are a permutation of [1,2,3..n] in increasing order, here the number in the ith place denotes that the ith-column queen is placed in the row with that number. 
*/

// User function Template for Java

class Solution {
    public ArrayList<ArrayList<Integer>> nQueen(int n) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        ArrayList<ArrayList<Integer>> board = new ArrayList<>();
        // Initialize the board with zeros
        for (int i = 0; i < n; i++) {
            board.add(new ArrayList<>(Collections.nCopies(n, 0)));
        }
        solveNQueens(board, res, n, 0);
        return res;
    }

    private boolean isSafe(ArrayList<ArrayList<Integer>> board, int r, int c, int n) {
        // Check the column
        for (int i = r - 1; i >= 0; i--) {
            if (board.get(i).get(c) == 1) {
                return false;
            }
        }

        // Check the upper-left diagonal
        int i = r - 1, j = c - 1;
        while (i >= 0 && j >= 0) {
            if (board.get(i).get(j) == 1) {
                return false;
            }
            i--;
            j--;
        }

        // Check the upper-right diagonal
        i = r - 1;
        j = c + 1;
        while (i >= 0 && j < n) {
            if (board.get(i).get(j) == 1) {
                return false;
            }
            i--;
            j++;
        }

        return true;
    }

    private void solveNQueens(ArrayList<ArrayList<Integer>> board, ArrayList<ArrayList<Integer>> res, int n, int row) {
        if (row == n) {
            // Convert the board configuration into a result
            ArrayList<Integer> solution = new ArrayList<>();
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    if (board.get(r).get(c) == 1) {
                        solution.add(c + 1); // Add column index (1-based)
                    }
                }
            }
            res.add(solution);
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isSafe(board, row, col, n)) {
                board.get(row).set(col, 1); // Place the queen
                solveNQueens(board, res, n, row + 1); // Recurse to the next row
                board.get(row).set(col, 0); // Backtrack (remove the queen)
            }
        }
    }
}
