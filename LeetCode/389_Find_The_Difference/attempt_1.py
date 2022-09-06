# O(n) time | O(1) space
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_Sum = 0
        for char in s:
            s_Sum += ord(char)
        
        t_Sum = 0
        for char in t:
            t_Sum += ord(char)
            
        return chr(t_Sum - s_Sum)
