# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []

    # O(1) time | O(1) space
    def peek(self):
        return self.stack[-1]

    # O(1) time | O(1) space
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    # O(1) time | O(1) space
    def push(self, number):
        currMin = number
        currMax = number

        if self.minMaxStack:
            currMin = min(number, self.minMaxStack[-1]['min'])
            currMax = max(number, self.minMaxStack[-1]['max'])

        self.minMaxStack.append({'min': currMin, 'max': currMax})
        self.stack.append(number)

    # O(1) time | O(1) space
    def getMin(self):
        if self.minMaxStack:
            return self.minMaxStack[-1]['min']
        else:
            return self.stack[-1]

    # O(1) time | O(1) space
    def getMax(self):
        if self.minMaxStack:
            return self.minMaxStack[-1]['max']
        else:
            return self.stack[-1]
