# O(n) time | O(1) space
# constant space due to constant-size 26 chars in alphabet
# can use maxf variable as opposed to finding max count of values every time in loop
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        left = 0
        maxf = 0
        
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])
            
            # while (right - left + 1) - max(count.values()) > k:
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            
        return res
