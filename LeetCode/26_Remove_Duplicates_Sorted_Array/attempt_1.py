# First Solution: O(n^2) time | O(1) space, bad time complexity due to re-shuffling of list after deletes
# Second Solution: O(n) time | O(1) space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
#         prev = nums[0]
#         idx = 1
        
#         while idx < len(nums):
#             if nums[idx] == prev:
#                 del nums[idx]
#             else:
#                 prev = nums[idx]
#                 idx += 1
        
#         return len(nums)

        prev = nums[0]
        idx = 1
        idxToReplace = 1
        
        while idx < len(nums):
            if nums[idx] == prev:
                idx += 1
            else:
                nums[idxToReplace] = nums[idx]
                prev = nums[idx]
                idxToReplace += 1
                idx += 1
        
        return idxToReplace
