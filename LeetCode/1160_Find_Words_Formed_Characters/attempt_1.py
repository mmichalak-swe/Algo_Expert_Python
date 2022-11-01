# O(n * m) time | O(1) space
# n is the len of words, m is the len of the longest word in words
# constant space because max space is 26 chars of alphabet
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charDict = {}
        output = 0
        
        for char in chars:
            charDict[char] = 1 + charDict.get(char, 0)

        for word in words:
            tempDict = {}
            flag = False
            for letter in word:
                if letter not in charDict:
                    flag = True
                    break
                else:
                    tempDict[letter] = 1 + tempDict.get(letter, 0)
            
            if flag:
                continue
            
            for letter in tempDict:
                if tempDict[letter] > charDict[letter]:
                    flag = True
                    break
            
            if not flag:
                output += len(word)
        
        return output
