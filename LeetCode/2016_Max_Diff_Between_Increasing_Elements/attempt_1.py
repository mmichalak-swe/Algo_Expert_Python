# O(n) time | O(1) space
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        lowNum = nums[0]
        highNum = float('-inf')
        maxDiff = -1
        
        for i in range(1, len(nums)):
            newDiff = nums[i] - lowNum

            if newDiff < 0:
                lowNum = nums[i]
            elif newDiff > 0:
                maxDiff = max(maxDiff, newDiff)
            
        return maxDiff if maxDiff != -1 else -1
