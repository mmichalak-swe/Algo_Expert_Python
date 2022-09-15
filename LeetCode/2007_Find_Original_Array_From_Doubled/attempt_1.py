from collections import Counter

# O(n*log(n)) time | O(n) space
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # if list is not of even length, original cannot exist
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        count = Counter(changed)
        output = []
        
        for num in changed:
            if count[num] >= 1:
                count[num] -= 1
                if count[num * 2] >= 1:
                    output.append(num)
                    count[num * 2] -= 1
            
        if len(output) == len(changed) // 2:
            return output
        
        return []
