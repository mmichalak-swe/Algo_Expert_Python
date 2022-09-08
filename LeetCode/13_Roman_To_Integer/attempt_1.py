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
        
        idx = 0
        while idx < len(s):
            print(idx)
            currChar = s[idx]
            nextChar = s[idx+1] if idx < len(s) - 1 else "Z"
            
            if currChar == "I" and nextChar in "VX":
                output += table[nextChar] - table[currChar]
                idx += 1
            elif currChar == "X" and nextChar in "LC":
                output += table[nextChar] - table[currChar]
                idx += 1
            elif currChar == "C" and nextChar in "DM":
                output += table[nextChar] - table[currChar]
                idx += 1
            else:
                output += table[currChar]
            
            idx += 1
        
        return output
