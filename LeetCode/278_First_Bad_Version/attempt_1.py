# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# O(log(n)) time | O(1) space
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left <= right:
            middle = (left + right) // 2
            value = isBadVersion(middle)
            
            if value is False:
                left = middle + 1
            elif value is True:
                right = middle - 1
            
        
        return left
