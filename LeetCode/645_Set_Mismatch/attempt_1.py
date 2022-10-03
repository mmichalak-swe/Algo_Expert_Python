# O(n) time | O(n) space
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
#         missing = None
        
#         noDuplicates = set(nums)
        
#         for num in range(1, len(nums) + 2):
#             if num not in noDuplicates:
#                 missing = num
#                 break
        
#         table = {n: False for n in nums}
        
#         for num in nums:
#             if table[num]:
#                 return [num, missing]
            
#             table[num] = True

# O(n) time | O(1) space
        n = len(nums)
        completeSum = n*(n+1) // 2              # sum up all numbers 1 to n
        missing = completeSum - sum(set(nums))
        duplicate = sum(nums) - sum(set(nums))

        return [duplicate, missing]
