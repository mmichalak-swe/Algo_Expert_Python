# O(n) time | O(1) space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = { 0: 0,
                   1: 0,
                   2: 0 }
        
        for num in nums:
            counts[num] += 1
        
        for i in range(len(nums)):
            if counts[0]:
                nums[i] = 0
                counts[0] -= 1
            elif counts[1]:
                nums[i] = 1
                counts[1] -= 1
            elif counts[2]:
                nums[i] = 2
                counts[2] -= 1
