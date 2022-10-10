# O(n) time | O(n) space
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        output = []
        idx1 = len(num1) - 1
        idx2 = len(num2) - 1
        carry = 0
        
        while idx1 >= 0 or idx2 >= 0:
            digit1 = num1[idx1] if idx1 >= 0 else 0
            digit2 = num2[idx2] if idx2 >= 0 else 0
            
            temp = int(digit1) + int(digit2) + carry
            
            output.append(temp % 10)
            
            carry = temp // 10
            
            idx1 -= 1
            idx2 -= 1
        
        if carry:
            output.append(carry)
            
        return ''.join([str(digit) for digit in output][::-1])
