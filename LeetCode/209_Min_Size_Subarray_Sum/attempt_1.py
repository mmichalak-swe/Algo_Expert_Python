# Sliding Window
# O(n) time | O(1) space
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        currSum = 0
        minSize = float('inf')
        
        while end <= len(nums):
            if currSum >= target:
                minSize = min(minSize, end - start)
                currSum -= nums[start]
                start += 1
            else:
                if end == len(nums):
                    break
                currSum += nums[end]
                end += 1
        
        return minSize if minSize != float('inf') else 0
