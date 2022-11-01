# O(n) time | O(1) space
# constant space due to max size of dict (26 chars in alphabet)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        letters = {}
        current = {}
        
        for char in s1:
            letters[char] = 1 + letters.get(char, 0)
        
        left = 0
        right = 0
        numMatching = 0
        
        while right < len(s2):
            # extend sliding window on the right
            addChar = s2[right]
            current[addChar] = 1 + current.get(addChar, 0)
            if current.get(addChar, 0) == letters.get(addChar, 0):
                numMatching += 1
                if numMatching == len(letters):
                    return True

            # shrink sliding window from the left
            if right - left + 1 == len(s1):
                removeChar = s2[left]
                if current.get(removeChar, 0) == letters.get(removeChar, 0):
                    numMatching -= 1
                current[removeChar] -= 1
                left += 1
            
            right += 1

        return False
