# Naive solution using built-in methods
class MinMaxStack:
    def __init__(self):
        self.stack = []

    # O(1) time | O(1) space
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # O(1) time | O(1) space
    def pop(self):
        return self.stack.pop()

    # O(1) time | O(1) space
    def push(self, number):
        self.stack.append(number)

    # O(n) time | O(1) space
    def getMin(self):
        return min(self.stack)

    # O(n) time | O(1) space
    def getMax(self):
        return max(self.stack)
