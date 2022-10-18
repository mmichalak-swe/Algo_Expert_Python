# O(n) time | O(1) space
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        letters = {letter: True for letter in sentence}
        return len(letters.keys()) == 26
