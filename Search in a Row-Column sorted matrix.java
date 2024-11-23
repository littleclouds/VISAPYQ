/* Given a 2D matrix mat[][], where every row and column is sorted in increasing order, and a number x the task is to find whether element x is present in the matrix or not.
  */

class Solution {
    public static boolean matSearch(int mat[][], int x) {
        // your code here
        if(mat==null || mat.length==0||mat[0].length==0){
            return false;
        }
        for(int i=0;i< mat.length;i++){
            for(int j=0;j< mat[i].length;j++){
                if(mat[i][j]==x){
                    return true;
                }
            }
        }
        return false;
    }
}
