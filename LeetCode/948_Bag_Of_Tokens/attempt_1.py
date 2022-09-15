# O(n*log(n)) time | O(1) space
# Possibly O(n) space due to Python's built-in sort using size N/2 temp array
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        left = 0
        right = len(tokens) - 1
        score = 0
        tokens.sort()
        
        while left <= right:
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1

            else: # power < tokens[left]
                if left == right or score == 0:
                    break
                
                power += tokens[right]
                score -= 1
                right -= 1
        
        return score
