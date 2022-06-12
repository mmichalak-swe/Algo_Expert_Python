
def multiStringSearch(bigString, smallStrings):
    output = [False for _ in smallStrings]
    trie = Trie()
    for word in smallStrings:
        trie.insert(word)

    idx = 0
    while idx < len(bigString):
        char = bigString[idx]
        if char == " " or char not in trie.root:
            idx += 1
            continue

        node = trie.root
        j = idx
        while j < len(bigString):
            if bigString[j] in node:
                node = node[bigString[j]]
            else:
                break
            if '*' in node:
                output[smallStrings.index(node['*'])] = True
            j += 1
        idx += 1

    return output

class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def insert(self, string):
        current = self.root
        for i in range(len(string)):
            if string[i] not in current:
                current[string[i]] = {}
            current = current[string[i]]
        current[self.endSymbol] = string
