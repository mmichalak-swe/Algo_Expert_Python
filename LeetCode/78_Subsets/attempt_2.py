# O(n * 2^n) time | O(2^n) space
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        subset = []
        
        def dfs(i):
            if i == len(nums):
                output.append(subset[:])
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # decision to not include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        
        return output
