### Brute-force method
### O(n) time | O(n) space
### insert method takes O(n) time, storing array of numbers, thus O(n) space
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.numbers = []

    def insert(self, number):
        self.numbers.append(number)
        self.numbers.sort()
        middle = len(self.numbers) // 2

        if len(self.numbers) % 2 == 0:
            self.median = (self.numbers[middle] + self.numbers[middle-1]) / 2
        else:
            self.median = self.numbers[middle]

    def getMedian(self):
        return self.median
