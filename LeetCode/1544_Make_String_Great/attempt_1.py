# O(n) time | O(n) space
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for char in s:
            if not stack:
                stack.append(char)
            elif stack[-1].isupper() and stack[-1].lower() == char:
                stack.pop()
            elif stack[-1].islower() and stack[-1].upper() == char:
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
