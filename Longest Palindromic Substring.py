''' Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. 
Incase of conflict, return the substring which occurs first ( with the least starting index ).'''

#User function Template for python3

class Solution:
    def longestPalindrome(self, a):
        # code here
        res=""
        resLen=0
        n=len(a)
        for i in range(n):
            
            #odd index
            l=i
            r=i
            
            while l>=0 and r<n and a[l]==a[r]:
                if r-l+1>resLen:
                    res=a[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
            
            l=i
            r=i+1
            
            while l>=0 and r<n and a[l]==a[r]:
                if r-l+1>resLen:
                    res=a[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
        return res
            
            
