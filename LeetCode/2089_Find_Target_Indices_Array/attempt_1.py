# O(n) time | O(1) space
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lt_count = eq_count = 0
        for n in nums:
            if n < target:
                lt_count += 1
            elif n == target:
                eq_count += 1
            
        return list(range(lt_count, lt_count+eq_count))
