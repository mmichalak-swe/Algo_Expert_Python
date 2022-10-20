# O(n * 2^n) time | O(n * 2^n) space
# better than above complexity due to avoiding duplicates
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                output.append(subset[:])
                return
            
            # all subsets that include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            dfs(i + 1)
        
        dfs(0)
        
        return output
