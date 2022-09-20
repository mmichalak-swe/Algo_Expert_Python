# O(n*m) time | O(1) space
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = 0
        
        while idx < len(haystack):
            if haystack[idx] == needle[0]:
                haystackIdx = idx
                needleIdx = 0
                while haystackIdx < len(haystack) and needleIdx < len(needle) and needle[needleIdx] == haystack[haystackIdx]:
                    needleIdx += 1
                    haystackIdx += 1
                
                if needleIdx == len(needle):
                    return idx
                    
            idx += 1
        
        return -1