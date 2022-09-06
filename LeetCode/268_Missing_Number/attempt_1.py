# First Solution - O(n*log(n)) time | O(1) space
# Second Solution - O(2n) time | O(1) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         endRange = len(nums)
        
#         currNum = 0
#         for i in range(endRange + 1):
#             try:
#                 if nums[i] != currNum:
#                     return currNum
#                 currNum += 1
#             except IndexError: # if i == endRange, the last num in the range is missing
#                 return endRange


        return sum(range(len(nums) + 1)) - sum(nums)
