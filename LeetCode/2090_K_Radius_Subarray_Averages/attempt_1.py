# O(n) time | O(n) space
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        preSum = [0] * (len(nums) + 1)
        output = [-1] * len(nums)
        
        for i, num in enumerate(nums):
            preSum[i + 1] = num + preSum[i]
        
        subtractIdx = 0
        for i in range(k, len(nums) - k):
            valToDeduct = preSum[subtractIdx]          # get amount to remove from currSum
            currSum = preSum[i + 1 + k] - valToDeduct  # calc correct sum through removal of necessary amount
            output[i] = currSum // (2*k + 1)

            subtractIdx += 1                           # increment subtractIdx in preSum for next iteration
            
        return output
