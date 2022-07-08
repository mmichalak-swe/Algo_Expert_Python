# O(n*k) time | O(m) space, where n is the number of words, k is the len of the longest
# word, and m is the number of unique characters
def minimumCharactersForWords(words):
    maxFreq = {}

    # O(n) time
    for word in words:
        tempCount = {}

        # O(k) time
        for char in word:
            if char not in tempCount:
                tempCount[char] = 1
            else:
                tempCount[char] += 1

        for char in tempCount:
            if char not in maxFreq:
                maxFreq[char] = tempCount[char]
            elif tempCount[char] > maxFreq[char]:
                maxFreq[char] = tempCount[char]

    # O(m) space
    return [char for char in maxFreq.keys() for i in range(maxFreq[char])]
