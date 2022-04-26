# Feel free to add new properties and methods to the class.
class MinMaxStack:

    ans = []

    def peek(self):
        return self.ans[0]

    def pop(self):
        return self.ans.pop(0)

    def push(self, number):
        self.ans.insert(0, number)
        pass

    def getMin(self):
        return min(self.ans)

    def getMax(self):
        return max(self.ans)

x = MinMaxStack()

x.push(2)
print(x.getMin())
print(x.getMax())