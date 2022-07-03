# Worst: O(2n*log(n)) -> O(nlog(n)) time | O(2n) -> O(n) space
# where n is the length of the input array
def groupAnagrams(words):
    sortedStrings = [''.join(sorted(word)) for word in words]
    anagramCount = {}
    output = []

    for i, string in enumerate(sortedStrings):
        if string in anagramCount:
            anagramCount[string].append(i)
        else:
            anagramCount[string] = [i]

    for anagram in anagramCount:
        output.append([])
        for idx in anagramCount[anagram]:
            output[-1].append(words[idx])

    return output
