from collections import deque

# O(n) time | O(n) space
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        
        output = deque()
        
        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                output.appendleft(nums[right] ** 2)
                right -= 1
            else:
                output.appendleft(nums[left] ** 2)
                left += 1
        
        return output
