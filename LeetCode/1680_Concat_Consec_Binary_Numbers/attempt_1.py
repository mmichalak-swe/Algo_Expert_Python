# O(n) time | O(n) space
class Solution:
    def concatenatedBinary(self, n: int) -> int:        
        stringList = []

        for i in range(1, n + 1):
            stringList.append(bin(i)[2:])
            
        stringConcat = ''.join(stringList)
        
        # int second argument is base of number converting from
        num = int(stringConcat, 2)
        
        return num % ((10 ** 9) + 7)
