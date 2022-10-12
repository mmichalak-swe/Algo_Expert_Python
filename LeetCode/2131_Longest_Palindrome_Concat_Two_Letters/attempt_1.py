# O(n) time | O(n) space
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        table = {}
        numPairs = 0
        
        # O(n) time | O(n) space
        for word in words:
            table[word] = 1 + table.get(word, 0)
        
        oddUsed = False

        # O(n) time
        for word in table:
            if word[0] != word[1] and table.get(word[::-1], 0) > 0:
                numPairs += min(table[word], table[word[::-1]]) * 2
                table[word[::-1]] = 0

            elif word[0] == word[1]:
                if table[word] & 1 and not oddUsed:
                    numPairs += table[word]
                    oddUsed = True
                else:
                    numPairs += (table[word] // 2) * 2

            table[word] = 0

        # only storing number of pairs in numPairs
        return numPairs * 2
