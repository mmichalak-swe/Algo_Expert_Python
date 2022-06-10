DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    print(trie.root)
    output = []
    visited = [[False for letter in row] for row in board]

    for row in range(len(board)):
        for col in range(len(board[row])):
            letter = board[row][col]

            if letter in trie.root:
                node = trie.root[letter]
                visited[row][col] = True
                validWord(board, visited, output, node, row, col, [letter])
                visited[row][col] = False
    return output


def validWord(board, visited, output, node, row, col, potentialWord):
    if '*' in node:
        if node['*'] not in output:
            output.append(node['*'])
            if len(node) == 1:
                del potentialWord[-1]
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
                potentialWord.append(potentialLetter)
                validWord(board, visited, output, node[potentialLetter], newRow, newCol, potentialWord)
        visited[newRow][newCol] = False
    if potentialWord:
        del potentialWord[-1]


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
