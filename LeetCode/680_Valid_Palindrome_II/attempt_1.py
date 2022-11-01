# O(n) time, O(1) space
# worst case, check for palindrome 2x, each idx in string only visited max of 2 times
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(string, left, right):
            while left < right:
                if string[left] != string[right]:
                    return False

                left += 1
                right -= 1
            
            return True
        
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s, left, right - 1) or isPalindrome(s, left + 1, right)
            
            left += 1
            right -= 1
        
        return True
