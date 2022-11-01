# O(n) time | O(1) space
# max difference includes first or last house
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
#         maxDiff = 0
#         firstColor = colors[0]
#         lastColor = colors[-1]
#         fromBeginning = None
#         fromEnd = None
        
#         for i in range(1, len(colors)):
#             if colors[i] != firstColor:
#                 fromBeginning = i
        
#         for i in range(len(colors) - 2, -1, -1):
#             if colors[i] != lastColor:
#                 fromEnd = i
        
#         return max(len(colors) - 1 - fromEnd, fromBeginning)

        fromEnd = 0
        fromBeginning = len(colors) - 1
        
        while colors[0] == colors[fromBeginning]:
            fromBeginning -= 1
        
        while colors[-1] == colors[fromEnd]:
            fromEnd += 1
        
        return max(len(colors) - 1 - fromBeginning, fromEnd)
