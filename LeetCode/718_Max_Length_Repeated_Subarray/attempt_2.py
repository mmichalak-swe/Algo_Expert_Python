# O(nm) time | O(min(n,m)) space, where n is the len of one input list,
# m is the len of the other
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        short = nums1 if len(nums1) < len(nums2) else nums2
        long = nums2 if len(nums2) > len(nums1) else nums1
        maxLength = 0

        board = [[0 for _ in range(len(short) + 1)] for _ in range(2)]
        
        for row in range(1, len(long) + 1):
            longPtr = row - 1
            for col in range(1, len(short) + 1):
                shortPtr = col - 1
                
                if short[shortPtr] == long[longPtr]:
                    board[1][col] = board[0][col-1] + 1
                    maxLength = max(maxLength, board[1][col])
                else:
                    board[1][col] = 0
                    
            board[0] = board[1][:]

        return maxLength
