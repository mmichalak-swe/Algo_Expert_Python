# O(n) time | O(n) space, where n is the length of the input string
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        output = []
        
        for i in range(numRows):
            output.append([])
            
        idx = 0
        outputIdx = 0
        step = -1

        while idx < len(s):
            output[outputIdx].append(s[idx])
            
            if outputIdx == 0 or outputIdx == len(output) - 1:
                step *= -1
                
            outputIdx += step
            idx += 1
        
        # print(output)
        
        return ''.join([''.join(x) for x in output])
