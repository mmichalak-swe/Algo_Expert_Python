# O(n) time | O(1) space
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # no valid answer if len == 1
        if len(palindrome) == 1:
            return ""
        
        for i, char in enumerate(palindrome):
            if char != 'a':
                if len(palindrome) % 2 != 0 and i == len(palindrome) // 2:
                    continue
                return palindrome[:i] + 'a' + palindrome[i+1:]

        # if palindrome is all 'a', return palindrome, but with last char changed to 'b'
        return palindrome[:-1] + 'b'
