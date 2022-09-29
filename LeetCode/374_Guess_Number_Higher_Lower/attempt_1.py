# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# O(log(n)) time | O(1) space
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right) // 2
            
            g = guess(mid)
            
            if g == -1:
                right = mid - 1
            elif g == 1:
                left = mid + 1
            else:
                return mid
