# O(2^n) time | O(2^n) space
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        output = []
        
        def backtrack(openNum, closedNum):
            if openNum == closedNum == n:
                output.append(''.join(stack))
                return
                
            if openNum < n:
                stack.append('(')
                backtrack(openNum + 1, closedNum)
                stack.pop()
            
            if closedNum < openNum:
                stack.append(')')
                backtrack(openNum, closedNum + 1)
                stack.pop()

        backtrack(0, 0)
        return output
