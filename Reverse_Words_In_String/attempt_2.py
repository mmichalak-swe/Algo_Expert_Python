# O(2n -> n) time | O(n) space, where n is the length of the input string
def reverseWordsInString(string):
    wordList = []
    idx = 0
    while idx != len(string):
        if string[idx] == ' ':
            wordList.append(' ')
            idx += 1
        elif string[idx] != ' ':
            sliceIdx = idx
            while idx != len(string) and string[idx] != ' ':
                idx += 1
            wordList.append(string[sliceIdx:idx])

    listReverse(wordList)
                
    return ''.join(wordList)


def listReverse(wordList):
    for i in range(len(wordList) // 2):
        wordList[i], wordList[len(wordList) - 1 - i] = wordList[len(wordList) - 1 - i], wordList[i]
