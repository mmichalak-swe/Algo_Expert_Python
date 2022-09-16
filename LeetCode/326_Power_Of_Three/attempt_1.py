# O(N) time | O(1) space, where N is the power 3 is raised to,
# that is greater than or equal to n
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 0:
            return False
        
        num = 1
        
        while num <= n:
            if num == n:
                return True

            num *= 3
            
        return False

    # cheesy solution
    # return n > 0 == 3**19 % n
