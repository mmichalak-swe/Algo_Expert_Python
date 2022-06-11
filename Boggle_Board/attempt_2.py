DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

# O(ws + nm*8^s) time | O(ws + nm) where w is # of words in words list, s is length
# of the longest word in the list, n is the width of the board, m is the height
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    output = {}
    visited = [[False for letter in row] for row in board]

    for row in range(len(board)):
        for col in range(len(board[row])):
            letter = board[row][col]

            if letter in trie.root:
                node = trie.root[letter]
                visited[row][col] = True
                validWord(board, visited, output, node, row, col)
                visited[row][col] = False
    return list(output.keys())


def validWord(board, visited, output, node, row, col):
    if '*' in node:
        output[node['*']] = True
        if len(node) == 1:
            return

    for direction in DIRECTIONS:
        newRow = row + direction[0]
        newCol = col + direction[1]

        if not (0 <= newRow < len(board)) or not (0 <= newCol < len(board[row])):
            continue
        if visited[newRow][newCol]:
            continue
        potentialLetter = board[newRow][newCol]
        visited[newRow][newCol] = True

        for candidate in node.keys():
            if potentialLetter == candidate:
                validWord(board, visited, output, node[potentialLetter], newRow, newCol)
        visited[newRow][newCol] = False


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr[self.endSymbol] = word
