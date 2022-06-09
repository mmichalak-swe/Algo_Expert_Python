from collections import deque

# O(wh) time | O(wh) space, where w = width, h = height of matrix
def minimumPassesOfMatrix(matrix):
    reqPasses = 0
    dataQueue = deque()

    x = len(matrix)
    y = len(matrix[0])

    # prime queueOne with all positives in matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            if matrix[row][col] > 0:
                dataQueue.append((row, col))

    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # only pop # of nodes off queue that were appended during
    # last pass through matrix
    while len(dataQueue):
        reqPasses += 1
        length = len(dataQueue)
        for i in range(length):
            curr = dataQueue.popleft()
            for direction in DIRECTIONS:
                searchRow = curr[0] + direction[0]
                searchCol = curr[1] + direction[1]
                if isValid(searchRow, searchCol, len(matrix), len(matrix[0])) and matrix[searchRow][searchCol] < 0:
                    matrix[searchRow][searchCol] *= -1
                    dataQueue.append((searchRow, searchCol))
            

    # subtract one from reqPasses due to one final pass after
    # all negatives changed to positives
    return reqPasses-1 if checkPositives(matrix) else -1


def isValid(row, col, x, y):
    return (0 <= row < x) and (0 <= col < y)


def queueJuggle(matrix, fromQueue, toQueue):
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while len(fromQueue):
        curr = fromQueue.popleft()
        for direction in DIRECTIONS:
            searchRow = curr[0] + direction[0]
            searchCol = curr[1] + direction[1]
            if isValid(searchRow, searchCol, len(matrix), len(matrix[0])) and matrix[searchRow][searchCol] < 0:
                matrix[searchRow][searchCol] *= -1
                toQueue.append((searchRow, searchCol))


def checkPositives(matrix):
    for row in matrix:
        for num in row:
            if num >= 0:
                continue
            else:
                return False
    return True
