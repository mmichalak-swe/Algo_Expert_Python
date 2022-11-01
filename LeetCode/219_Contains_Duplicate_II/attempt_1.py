# O(n) time | O(n) space
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        table = {}
        
        left = 0
        right = 0
        
        while right < len(nums):
            if nums[right] in table and table[nums[right]] > 0:
                return True
            
            table[nums[right]] = 1 + table.get(nums[right], 0)
            
            if right >= k:
                if table[nums[left]] > 0:
                    table[nums[left]] -= 1
                left += 1
            
            right += 1
        
        return False
