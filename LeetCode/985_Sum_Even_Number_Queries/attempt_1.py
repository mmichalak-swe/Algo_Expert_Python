# O(n + m) time | O(1) space, where n is the len of nums,
# and m is the len of queries
# building the output doesn't count as the function doesn't use it execute
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        output = []
        evenSum = sum(num for num in nums if num % 2 == 0)
        
        for val, idx in queries:
            currNum = nums[idx] 
            newNum = currNum + val
            nums[idx] = newNum
            
            if newNum % 2 == 0: # newNum needs to be added to evenSum
                evenSum += newNum
            if currNum % 2 == 0:
                evenSum -= currNum   
            
            output.append(evenSum)

        return output
