# O(N) time | O(N) space
# where N is the number of elements in the input matrix
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS, self.COLS = len(matrix), len(matrix[0])
        self.matrix = matrix
        
        self.sums = [[0 for c in range(self.COLS + 1)] for r in range(self.ROWS + 1)]

        for row in range(self.ROWS):
            prefix = 0
            for col in range(self.COLS):
                prefix += self.matrix[row][col]
                above = self.sums[row][col + 1]
                self.sums[row + 1][col + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        baseSum = self.sums[row2][col2]
        above = self.sums[row1 - 1][col2]
        left = self.sums[row2][col1 - 1]
        addBack = self.sums[row1 - 1][col1 - 1]
        
        return baseSum - above - left + addBack


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)