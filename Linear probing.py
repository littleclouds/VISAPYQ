''' Given an array KEYS consisting of N non-negative integers. For each element in a given array, you need to determine the index by which this element is mapped in the hash table if the ‘Linear Probing’ technique is used to handle collision. The hash function you need to consider is H(X) = X mod N i.e. index = X mod N. 
Return an array ‘HASH_TABLE’ of size N in which: HASH_TABLE[ i ] = KEYS[ j ] where, i = KEYS[ j ] mod N.
'''
def linear_probing(keys, n):
    hash_table = [-1] * n  # Initialize hash table with -1 to indicate empty slots

    for key in keys:
        index = key % n
        while hash_table[index] != -1:
            index = (index + 1) % n  # Linear probing
        hash_table[index] = key

    return hash_table

# Example usage
if __name__ == "__main__":
    keys = [5, 3, 2, 6, 4]
    n = 5
    hash_table = linear_probing(keys, n)
    print("Hash Table:", hash_table)
