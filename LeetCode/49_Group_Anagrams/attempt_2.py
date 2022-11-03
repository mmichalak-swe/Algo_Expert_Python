# O(m * n) time | O(n) space
# n is num of words, m is avg len of word
# time complexity is multiplied by 26 for num of chars in alphabet, drop constant from TC
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for word in strs:
            chars = [0] * 26
            for char in word:
                chars[ord(char) - ord('a')] += 1

            # can't use lists as dict keys, convert chars to tuple
            table[tuple(chars)].append(word)
        
        return table.values()
