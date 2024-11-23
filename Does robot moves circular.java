/* Given a sequence of moves for a robot. Check if the sequence is circular or not.

A sequence of moves is circular if the first and last positions of the robot are the same. A move can be one of the following :
    G - Go one unit
    L - Turn left
    R - Turn right
  You don't need to read input or print anything. Your task is to complete the function isCircular() which takes the string path as input and returns "Circular" if the path is circular else returns "Not Circular".

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |S| ≤ 105
  */



//User function Template for Java

class Solution
{
    public String isCircular(String s)
    {
        int x=0,y=0,d=0;
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};
        for(char c : s.toCharArray()){
            if(c=='G'){
                x+=dx[d];
                y+=dy[d];
            }else if(c=='L'){
                d=(d+3)%4;
            }else{
                d=(d+1)%4;
            }
        }
        return (x==0 && y==0)?"Circular":"Not Circular";
        //code here
    }
}
