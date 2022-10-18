# O(n^2) time | O(1) space
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        output = []
        
        for top in range(1, n):
            for bottom in range(top + 1, n + 1):
                
                if top % 2 == 0 and bottom % 2 == 0:
                    continue
                
                flag = False
                for num in range(3, bottom + 1, 2):
                    if top % num == 0 and bottom % num == 0:
                        flag = True
                        break
                
                if not flag:
                    output.append(str(top) + '/' + str(bottom))
                
        return output
