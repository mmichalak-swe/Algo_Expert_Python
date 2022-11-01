# O(n^2) time | O(1) space

from math import gcd

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        output = []
        
        for top in range(1, n):
            for bottom in range(top + 1, n + 1):

                if gcd(top, bottom) == 1:
                    output.append(str(top) + '/' + str(j=bottom))
                
        return output
