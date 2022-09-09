# O(N) time | O(N) space, where N is the total number of combinations of the letters
# O(3^n) time (approx) where n is the number of digits in the input str
# Could be 4^n counting 7 and 9
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        table = {'2': 'abc',
                 '3': 'def',
                 '4': 'ghi',
                 '5': 'jkl',
                 '6': 'mno',
                 '7': 'pqrs',
                 '8': 'tuv',
                 '9': 'wxyz'}
            
        output = []
        
        def recursiveHelper(digits, idx, prevStr):
            if idx == len(digits):
                output.append(''.join(prevStr))
                return
            
            for char in table[digits[idx]]:
                prevStr.append(char)
                recursiveHelper(digits, idx + 1, prevStr)
                prevStr.pop()
                
        recursiveHelper(digits, 0, [])
        return output
