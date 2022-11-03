# O(n) time | O(k) space
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        out = []
        
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop() # popped from d because d has elements and nums[d.top] < current element
            
            d.append(i) # add i to d
            
            if d[0] == i - k:
                d.popleft() # popped left from d because it's to the left of the window (i-k)
            
            if i >= k - 1:
                out.append(nums[d[0]]) # append nums[d[0]] to out
        
        return out
