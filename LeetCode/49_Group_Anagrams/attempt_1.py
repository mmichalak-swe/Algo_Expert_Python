# O(m * nlog(n)) time | O(n) space
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            anagrams[sortedWord].append(word)

        return list(anagrams.values())
