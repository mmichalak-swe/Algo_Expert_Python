# O(p + s) time | O(p) space, where p is the len of the pattern,
# s is the length of the string.split()
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_List, table = s.split(), {}
        
        if len(pattern) != len(s_List):
            return False
        
        if len(set(pattern)) != len(set(s_List)): # catches "abba", "cat, cat, cat, cat"
            return False

        for idx in range(len(pattern)):
            char = pattern[idx]
            if char not in table:
                table[char] = s_List[idx]
            else:
                if table[char] != s_List[idx]:
                    return False
        
        return True
