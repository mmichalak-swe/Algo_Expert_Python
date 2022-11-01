# O(n) time | O(1) space
class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = set()
        
        # chars with even counts will not appear in set
        for letter in s:
            if letter not in table:
                table.add(letter)
            else:
                table.remove(letter)
        
        # can at most add one extra occurence of one of the odd counts in
        return len(s) - len(table) + 1 if table else len(s)
