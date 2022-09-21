# O(max(n,m)) time | O(1) space
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_Size = len(s)
        t_Size = len(t)
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < s_Size and ptr2 < t_Size:
            if s[ptr1] == t[ptr2]:
                ptr1 += 1
            ptr2 += 1
        
        return ptr1 == len(s)
