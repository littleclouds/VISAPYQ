'''
Given a string s, your task is to find the longest palindromic substring within s. 
A substring is a contiguous sequence of characters within a string, defined as s[i...j] where 0 ≤ i ≤ j < len(s).
A palindrome is a string that reads the same forward and backward. More formally, s is a palindrome if reverse(s) == s.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        
        return s[start:end + 1]
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "babad"
    print("Longest Palindromic Substring of", s, "is:", solution.longestPalindrome(s))
