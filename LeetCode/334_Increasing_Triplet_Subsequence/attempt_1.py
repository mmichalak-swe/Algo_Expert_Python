# O(n) time | O(n) space
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        runningMax = [nums[-1]] * (len(nums) + 1)
        
        for i in range(len(nums) - 1, 1, -1):
            runningMax[i] = max(nums[i], runningMax[i + 1])

        runningMin = nums[0]
        
        for i in range(1, len(nums) - 1):
            if runningMin < nums[i] < runningMax[i + 1]:
                return True
            
            runningMin = min(runningMin, nums[i])
        
        return False
