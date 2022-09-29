# O(n) time | O(n) space
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        output = 0
        maxSoFar = nums[0]
        minRemain = [nums[-1] for num in nums]
        
        for i in range(len(minRemain) - 2, -1, -1):
            minRemain[i] = min(nums[i+1], minRemain[i+1])
        
        for i in range(1, len(nums) - 1):
            if maxSoFar < nums[i] < minRemain[i]:
                output += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                output += 1
            else:
                output += 0
            
            maxSoFar = max(maxSoFar, nums[i])

        return output
