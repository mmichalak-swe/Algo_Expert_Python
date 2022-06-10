# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.

# Searching = O(m) time | O(1) space - m is length of string we are searching for
# Creation = O(n^2) time | O(n^2) space - where n in length of input string,
# could be O(n) space if string is all repeating characters

# A suffix Trie can be built in O(n) time with complex algos

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        length = len(string)

        for i in range(length):
            node = self.root
            for j in range(i, length):
                letter = string[j]
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node
