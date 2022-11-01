# O(n) time | O(n) space
# keeps track of most recent index of n, if <= k, return True
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_dict = {}

        for i, n in enumerate(nums):
            if n in index_dict and i - index_dict[n] <= k:
                return True

            index_dict[n] = i

        return False
