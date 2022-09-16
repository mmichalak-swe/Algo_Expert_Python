# O(n) time | O(1) space
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s) - 1
        size = 0
        end = False
        
        while idx >= 0:
            if s[idx] == ' ':
                if end:
                    break
                idx -= 1

            elif s[idx] != ' ':
                idx -= 1
                size += 1
                end = True

            else:
                break
        
        return size
