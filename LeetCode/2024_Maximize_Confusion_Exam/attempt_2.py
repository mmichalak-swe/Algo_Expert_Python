# O(n) time | O(1) space
# max of 2 key-value pairs in the counts dict
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxWindow = 0
    
        counts = {}
        
        left = 0
        for right in range(len(answerKey)):
            counts[answerKey[right]] = 1 + counts.get(answerKey[right], 0)

            # Don't need to shrink window, as even if a smaller valid window is found, it doesn't matter
            # just increment left 1 if current window is invalid
            if counts.get('T', 0) > k and counts.get('F', 0) > k:
                counts[answerKey[left]] -= 1
                left += 1
            else:
                maxWindow = max(maxWindow, right - left + 1)
        
        return maxWindow
