# O(n) time | O(n) space
class Solution:
    def reverseVowels(self, s: str) -> str:
        charList = [char for char in s]
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        locations = []
        
        for i, char in enumerate(charList):
            if char in vowels:
                locations.append(i)
        
        left = 0
        right = len(locations) - 1
        
        while left < right:
            charList[locations[left]], charList[locations[right]] = charList[locations[right]], charList[locations[left]]
            left += 1
            right -= 1
        
        return ''.join(charList)
