class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxWindow = 0
        
        counts = {}
        
        left = 0
        for right in range(len(nums)):
            counts[nums[right]] = 1 + counts.get(nums[right], 0)
            
            # Don't need to shrink window, as even if a smaller valid window is found, it doesn't matter
            # just increment left 1 if current window is invalid
            if counts.get(0, 0) > k:
                counts[nums[left]] -= 1
                left += 1
            else:
                maxWindow = max(maxWindow, right - left + 1)

        return maxWindow
