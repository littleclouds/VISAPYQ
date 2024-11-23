/* Given an integer n, denoting the number of cuts that can be made on a pancake, 
find the maximum number of pieces that can be formed by making n cuts.
NOTE: Cuts can't be horizontal.*/ 

class Solution
{
    public int maximum_Cuts(int n){
        if(n<0) return 0;
        if(n==0) return 1;
        return (n*(n+1))/2+1;
    }
}
