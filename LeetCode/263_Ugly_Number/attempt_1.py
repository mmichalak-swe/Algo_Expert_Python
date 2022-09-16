# O(n) time | O(1) space, where n is the number of factors of n,
# that we end up dividing by
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for num in (10, 5, 4, 3, 2):
            while n % num == 0:
                n /= num
        
        return abs(n) == 1
