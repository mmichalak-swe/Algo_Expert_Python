# O(1) time | O(1) space
class Solution:
    def maximum69Number (self, num: int) -> int:
        sixIdx = -1
        temp = num
        i = 0
        
        while temp > 0:
            if temp % 10 == 6:
                sixIdx = i
            temp = temp // 10
            i += 1
        
        return num + 3 * (10 ** sixIdx) if sixIdx != -1 else num
