# O(n*m) time | O(m) space, where m is the length of the longest sequence
class Solution:
    def countAndSay(self, n: int) -> str:
        
        def intToDigitsHelper(string):
            temp = []
            
            count = 1
            for i in range(1, len(string)):
                if string[i] == string[i-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(string[i-1])
                    count = 1

            temp.append(str(count))
            temp.append(string[-1])
            return ''.join(temp)
        
        output = '1'
        for i in range(n-1):
            output = intToDigitsHelper(output)
        
        return output
