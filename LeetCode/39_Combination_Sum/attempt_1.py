# O(n^t) time | O(t) space, where t is the target value, n is num of candidates
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def recursiveHelper(idx, currSum, currList):
            if idx == len(candidates):
                return
            
            if currSum > target:
                return
            
            if currSum == target:
                output.append(currList)
                return
            
            recursiveHelper(idx, currSum + candidates[idx], currList + [candidates[idx]])
            recursiveHelper(idx+1, currSum, currList)
            
        recursiveHelper(0, 0, [])
        return output
