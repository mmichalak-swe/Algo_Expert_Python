def multiStringSearch(bigString, smallStrings):
    output = [False for _ in smallStrings]
    trie = makeTrieString(smallStrings)

    idx = 0
    while idx < len(bigString):
        char = bigString[idx]
        if char == " " or char not in trie:
            idx += 1
            continue

        node = trie
        j = idx
        possibility = []
        while j < len(bigString):
            if bigString[j] in node:
                possibility.append(bigString[j])
                node = node[bigString[j]]
            else:
                break
            if ''.join(possibility) in smallStrings:
                wordInSmall = ''.join(possibility)
                output[smallStrings.index(wordInSmall)] = True
            if node == {}:
                break
            j += 1
        idx += 1

    return output


def makeTrieString(smallStrings):
    trie = {}
    for word in smallStrings:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
    return trie
