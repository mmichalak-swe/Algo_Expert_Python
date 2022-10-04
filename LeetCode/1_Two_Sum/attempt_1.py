# O(n) time | O(n) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            difference = target - num
            if num in seen:
                return [seen[num], i]
            else:
                seen[difference] = i
