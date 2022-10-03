# O(s + t) time | O(1) space
# constant space due to max dict size of 26 (chars in alphabet)
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        if len(target) > len(s):
            return 0

        sCount, tCount = {}, {}

        for char in s:
            sCount[char] = 1 + sCount.get(char, 0)
        
        for char in target:
            if char not in sCount:
                return 0
            tCount[char] = 1 + tCount.get(char, 0)
        
        output = float('inf')
        
        for char in target:
            output = min(output, sCount[char] // tCount[char])
        
        return output
