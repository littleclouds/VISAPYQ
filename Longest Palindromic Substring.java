/* Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). 
Palindrome string: A string which reads the same backwards. 
More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index ).
*/



//User function Template for Java

class Solution{
    int max=0,start=0,end=0;
    String longestPalindrome(String S){
        // code here
        int n=S.length();
        for(int i=0;i<n;i++)
        {
            for(int j=i;j<n;j++)
            {
                if(isPalidrome(S,i,j))
                {
                    if((j-i)+1>max)
                    {
                        max=(j-i)+1;
                        start=i;
                        end=j;
                    }
                }
            }
        }
        return S.substring(start,end+1);
        
    }
    static boolean isPalidrome(String s,int left,int right)
    {
        while(left<right)
        {
            if(s.charAt(left)!=s.charAt(right))
            {
                return false;
            }
            else
            {
                left++;
                right--;
            }
        }
        return true;
    }
}
