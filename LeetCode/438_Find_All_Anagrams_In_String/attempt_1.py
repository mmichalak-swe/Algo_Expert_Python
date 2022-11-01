# O(n) time | O(1) space
# O(1) space comes from constant 26 chars in alphabet
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        table = {}
        end = 0
        start = 0
        output = []

        for char in p:
            table[char] = 1 + table.get(char, 0)

        currAna = {}
        numMatching = 0
        target = len(set(p))

        while end < len(s):
            char = s[end]
            if char in table:
                currAna[char] = 1 + currAna.get(char, 0)
                if currAna[char] == table[char]:
                    numMatching += 1
                    if numMatching == target:
                        output.append(start)

            end += 1
            if end - start == len(p):
                char = s[start]
                if char in table and currAna[char] == table[char]:
                    numMatching -= 1
                    currAna[char] -= 1
                elif char in table:
                    currAna[char] -= 1
                start += 1

        return output
