# O(log(n)) time | O(1) space
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left = 0
        right = x
        
        while left < right:
            middle = (left + right) // 2
            
            if middle * middle > x:
                right = middle
            elif middle * middle < x:
                left = middle + 1
            else:
                return middle

        return left - 1
