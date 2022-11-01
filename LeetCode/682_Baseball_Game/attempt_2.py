# O(n) time | O(n) space
# keep track of output as going along as opposed to sum(stack) should be faster
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        output = 0
        
        for op in operations:
            if op.isalpha():
                if op == 'C':
                    output -= stack.pop()
                elif op == 'D':
                    stack.append(stack[-1] * 2)
                    output += stack[-1]
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
                output += stack[-1]
            else:
                stack.append(int(op))
                output += int(op)
        
        return output
