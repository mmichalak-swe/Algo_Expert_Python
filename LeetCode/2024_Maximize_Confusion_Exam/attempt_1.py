# O(n) time | O(1) space
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def helper(answerKey, k, keep):
            left = 0
            right = 0
            streak = 0

            while right < len(answerKey):
                if answerKey[right] == keep:
                    right += 1
                else:
                    if k > 0:
                        right += 1
                        k -= 1
                    else:
                        while answerKey[left] == keep:
                            left += 1
                        left += 1
                        k += 1
                        
                streak = max(streak, right - left)

            return streak


        return max(helper(answerKey, k, 'T'), helper(answerKey, k, 'F'))
