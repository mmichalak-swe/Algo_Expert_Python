class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[-1]
        
        numMatching = 0
        stop = False

        for zeroIdx in range(len(strs[0])):
            currChar = strs[0][zeroIdx]

            for matchIdx in range(1, len(strs)):
                if zeroIdx >= len(strs[matchIdx]) or strs[matchIdx][zeroIdx] != currChar:
                    stop = True
                    break
            
            if stop:
                break
            
            numMatching += 1

        return strs[0][:numMatching]
