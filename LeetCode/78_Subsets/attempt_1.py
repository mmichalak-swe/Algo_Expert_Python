# O(n*2^n) time | O(n*2^n) space
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        # for num in nums:
        #     control = len(output)
        #     for i in range(control):
        #         newItem = output[i][:]
        #         newItem.append(num)
        #         output.append(newItem)
        
        for num in nums:
            for i in range(len(output)):
                curr = output[i]
                output.append(curr + [num])
        
        # for num in nums:
        #     output += [item + [num] for item in output]

        return output
