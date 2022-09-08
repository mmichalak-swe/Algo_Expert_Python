# O(n) time | O(1) space, where n is the length of the input string
class Solution:
    def romanToInt(self, s: str) -> int:
        table = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000
                }
        
        output = 0
        
        for i in range(len(s) - 1):
            if table[s[i]] < table[s[i + 1]]:
                output -= table[s[i]]
            else:
                output += table[s[i]]
        
        output += table[s[-1]]
        
        return output
