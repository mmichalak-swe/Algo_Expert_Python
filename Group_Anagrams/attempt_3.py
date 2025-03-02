# O(w * n * log(n)) time | O(wn) space, where w is the number of words, and
# n is the length of the longest word
def group_anagrams(words: list[str]) -> list[str]:
    anagrams = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())
