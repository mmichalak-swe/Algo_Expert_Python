# O(n*n!) time | O(n!) space
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
        
#         output = []
        
#         if len(nums) == 1:
#             return [nums[:]]
        
#         for i in range(len(nums)):
#             n = nums.pop(0)
#             perms = self.permute(nums)
        
#             for perm in perms:
#                 perm.append(n)

#             output.extend(perms)
#             nums.append(n)
    
#         return output

def permute(nums):
    output = []
    
    if len(nums) == 1:
        return [nums[:]]
    
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
    
        for perm in perms:
            perm.append(n)

        output.extend(perms)
        nums.append(n)

    return output

x = [1, 2, 3]

print(permute(x))