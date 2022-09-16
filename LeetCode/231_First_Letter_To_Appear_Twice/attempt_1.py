# O(n) time, O(1) space
# constant space due to constant size alphabet (26 chars max in table)
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        table = {}
        
        for char in s:
            if char not in table:
                table[char] = True
            else:
                return char
