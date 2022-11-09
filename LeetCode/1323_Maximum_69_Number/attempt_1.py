# O(n) time | O(n) space
class Solution:
    def maximum69Number (self, num: int) -> int:
        numString = [digit for digit in str(num)]
        
        for i, digit in enumerate(numString):
            if digit != '9':
                numString[i] = '9'
                break
        
        return int(''.join(numString))
