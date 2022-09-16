# O(n) time | O(1) space
# constant space considering alphabet only has 26 chars
class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = {}
        
        for char in s:
            table[char] = 1 + table.get(char, 0)
        
        for idx in range(len(s)):
            if table[s[idx]] == 1:
                return idx
    
        return -1
