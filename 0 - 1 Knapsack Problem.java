/* You are given the weights and values of items, and you need to put these items in a knapsack of capacity capacity to achieve the maximum total value in the knapsack. 
Each item is available in only one quantity.
In other words, you are given two integer arrays val[] and wt[], which represent the values and weights associated with items, respectively. 
You are also given an integer capacity, which represents the knapsack capacity. Your task is to find the maximum sum of values of a subset of val[] such that the sum of the weights of the corresponding subset is less than or equal to capacity. 
You cannot break an item; you must either pick the entire item or leave it (0-1 property). */

public class Knapsack {
    // Function to return max value that can be put in knapsack of capacity
    static int knapSack(int capacity, int wt[], int val[], int n) {
        int K[][] = new int[n + 1][capacity + 1];

        // Build table K[][] in bottom-up manner
        for (int i = 0; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {
                if (i == 0 || w == 0)
                    K[i][w] = 0;
                else if (wt[i - 1] <= w)
                    K[i][w] = Math.max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
                else
                    K[i][w] = K[i - 1][w];
            }
        }

        return K[n][capacity];
    }

    // Driver code
    public static void main(String args[]) {
        int val[] = new int[]{60, 100, 120};
        int wt[] = new int[]{10, 20, 30};
        int capacity = 50;
        int n = val.length;
        System.out.println(knapSack(capacity, wt, val, n));
    }
}
