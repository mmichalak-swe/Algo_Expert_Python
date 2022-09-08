# O(n) time | O(n) space, where n is the length of x when x converted to a str
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        
        x *= sign
        
        newX = sign * int(str(x)[::-1])
        
        lowerBound = -2 ** 31
        upperBound = (2 ** 31) - 1
        
        return newX if lowerBound <= newX <= upperBound else 0
