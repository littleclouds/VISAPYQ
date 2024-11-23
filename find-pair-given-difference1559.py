'''
Given an array, arr[] and an integer x, return true if there exists a pair of elements in the array whose absolute difference is x, otherwise, return false.
Constraints:
1<= arr.size() <=106 
1<= arr[i] <=106 
0<= x <=105
'''

from typing import List
class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        seen = set()
    
        for num in arr:
        # Check if num + x or num - x is in the set
            if num + x in seen or num - x in seen:
                return True
        
        # Add the current element to the set for future comparisons
            seen.add(num)
    
    # If no pair is found
        return False
      
