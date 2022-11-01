# O(n) time | O(1) space
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:        
        # beacuse palindrome, only need to check first half in loop
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]

        # if palindrome is all 'a', return palindrome, but with last char changed to 'b'
        # covers case where len(palindrome) == 1, p[:-1] will evaluate to ""
        return palindrome[:-1] + 'b' if palindrome[:-1] else ""
