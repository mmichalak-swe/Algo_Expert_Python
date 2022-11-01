# O(n) time | O(n) space
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        
        for i in range(1, len(s)):
            if stack and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)
