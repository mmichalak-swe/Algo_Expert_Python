# O(n*k) time | O(m) space, where n is the number of words, k is the len of the longest
# word, and m is the number of unique characters
def minimumCharactersForWords(words):
    dictOfChars = {}

    # O(n) time
    for word in words:
        tempDict = {}

        # O(k) time
        for char in word:
            if char not in tempDict:
                tempDict[char] = 1
            else:
                tempDict[char] += 1

        for char in tempDict:
            if char not in dictOfChars:
                dictOfChars[char] = tempDict[char]
            elif tempDict[char] > dictOfChars[char]:
                dictOfChars[char] = tempDict[char]

    # O(m) space
    output = [char for char in dictOfChars.keys() for i in range(dictOfChars[char])]

    return output
