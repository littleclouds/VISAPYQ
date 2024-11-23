/* Given an unsorted array arr containing only non-negative integers, your task is to find a continuous subarray 
(a contiguous sequence of elements) whose sum equals a specified value target. 
You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. */

class Solution {
    static ArrayList<Integer> subarraySum(int[] a, int k) {
        long s=0;
        for(int l=0,r=0;;){
            
            if(s<k){
                if (r<a.length){
                    // System.out.println(s+" +"+a[r]);
                    s+=a[r++];
                } else break;
            } else if (s>k){
                // System.out.println(s+" -"+a[l]);
                s-=a[l++];
            } else {
                return new ArrayList<Integer>(Arrays.asList(l+1,r));
            }
        }
        return new ArrayList<Integer>(Arrays.asList(-1));
    }
}
