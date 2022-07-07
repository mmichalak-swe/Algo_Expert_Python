# O(2n -> n) time | O(n) space, where n is the length of the input string
def reverseWordsInString(string):
    wordList = []
    idx = 0
    while idx != len(string):
        temp = ''
        if string[idx] == ' ':
            while idx != len(string) and string[idx] == ' ':
                temp += ' '
                idx += 1
            wordList.append(temp)
        elif string[idx] != ' ':
            while idx != len(string) and string[idx] != ' ':
                temp += string[idx]
                idx += 1
            wordList.append(temp)

    output = ""
    for i in range(len(wordList) - 1, -1, -1):
        output += wordList[i]
                
    return output
