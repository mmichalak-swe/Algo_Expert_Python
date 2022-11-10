# O(n) time | O(n) space
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        
        return ''.join(stack)
