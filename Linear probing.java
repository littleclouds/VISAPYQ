/* Given an array KEYS consisting of N non-negative integers. 
For each element in a given array, you need to determine the index by which this element is mapped in the hash table if the ‘Linear Probing’ technique is used to handle collision. 
The hash function you need to consider is H(X) = X mod N i.e. index = X mod N. 
Return an array ‘HASH_TABLE’ of size N in which: HASH_TABLE[ i ] = KEYS[ j ] where, i = KEYS[ j ] mod N. */

import java.util.Arrays;

public class LinearProbing {
    public int[] linearProbing(int[] keys, int n) {
        int[] hashTable = new int[n];
        Arrays.fill(hashTable, -1); // Initialize hash table with -1 to indicate empty slots

        for (int key : keys) {
            int index = key % n;
            while (hashTable[index] != -1) {
                index = (index + 1) % n; // Linear probing
            }
            hashTable[index] = key;
        }

        return hashTable;
    }

    // Driver code
    public static void main(String[] args) {
        LinearProbing solution = new LinearProbing();
        int[] keys = {5, 3, 2, 6, 4};
        int n = 5;
        int[] hashTable = solution.linearProbing(keys, n);
        System.out.println("Hash Table: " + Arrays.toString(hashTable));
    }
}
