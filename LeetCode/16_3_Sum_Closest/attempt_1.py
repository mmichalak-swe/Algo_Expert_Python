# O(n^2) time | O(1) space
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]

                if abs(target - currSum) < abs(closest - target):
                    closest = currSum
                    
                if currSum < target:
                    left += 1
                elif currSum > target:
                    right -= 1
                else:
                    return currSum
        
        return closest
