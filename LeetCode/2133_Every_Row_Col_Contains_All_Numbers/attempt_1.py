class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # function to validate rows, cols
        def isValid(items):
            return len(set(items)) == len(items)
        
        # validate rows
        for row in matrix:
            if not isValid(row):
                return False
        
        # validate cols
        for col in zip(*matrix):
            if not isValid(col):
                return False

        return True
