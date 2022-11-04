# O(n) time | O(n) space
class Solution:
    def reverseVowels(self, s: str) -> str:
        charList = [char for char in s]
        vowels = {'a', 'e', 'i', 'o', 'u'}

        left = 0
        right = len(charList) - 1
        
        while left < right:
            lC = charList[left]
            rC = charList[right]
            
            if not lC.isalpha() or lC.lower() not in vowels:
                left += 1
                continue
            if not rC.isalpha() or rC.lower() not in vowels:
                right -= 1
                continue

            charList[left], charList[right] = charList[right], charList[left]
            left += 1
            right -= 1
        
        return ''.join(charList)
