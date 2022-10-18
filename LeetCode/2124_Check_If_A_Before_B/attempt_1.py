# O(n) time | O(1) space
class Solution:
    def checkString(self, s: str) -> bool:
        lastA = None
        firstB = None
        
        for idx, char in enumerate(s):
            if char == 'a':
                lastA = idx
            else:
                if not firstB:
                    firstB = idx
        
        if lastA is None or firstB is None:
            return True
        
        return lastA < firstB
