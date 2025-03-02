# Worst: O(2n*log(n)) -> O(nlog(n)) time | O(2n) -> O(n) space
# where n is the length of the input array
def group_anagrams(words: list[str]) -> list[str]:
    sorted_strings = [''.join(sorted(word)) for word in words]
    anagram_count = {}
    output = []

    for i, string in enumerate(sorted_strings):
        if string in anagram_count:
            anagram_count[string].append(i)
        else:
            anagram_count[string] = [i]

    for anagram in anagram_count:
        output.append([])
        for idx in anagram_count[anagram]:
            output[-1].append(words[idx])

    return output
