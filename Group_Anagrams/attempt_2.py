# O(w * n * log(n)) time | O(wn) space, where w is the number of words, and
# n is the length of the longest word
def group_anagrams(words: list[str]) -> list[str]:
    sorted_words = [''.join(sorted(word)) for word in words]
    anagrams = {}

    for i, word in enumerate(sorted_words):
        if word in anagrams:
            anagrams[word].append(words[i])
        else:
            anagrams[word] = [words[i]]

    return list(anagrams.values())
