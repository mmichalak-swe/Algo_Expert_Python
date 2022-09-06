# First Solution - O(n) time | O(n/2) space
# worst case O(n/2) space, best case O(1) space

# Second Solution - O(n) time | O(1) space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         seen = {}
        
#         for num in nums:
#             if num in seen:
#                 del seen[num]
#             else:
#                 seen[num] = True

#         return list(seen.keys())[0]


        output = 0

        for num in nums:
            output ^= num

        return output
