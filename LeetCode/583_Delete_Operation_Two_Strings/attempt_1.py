# Brute Force: O(2^len1 + 2^len2) time | O(max(len1, len2))
# Optimized: O(len1 * len2) time | O(len1 * len2) space
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        dp = [[None] * (len2 + 1) for i in range(len1 + 1)]

        def recur(word1, word2, i, j):
            if i == len1 and j == len2:
                return 0
            if i == len1 or j == len2:
                return max(len1 - i, len2 - j)
            if dp[i][j] is not None:
                return dp[i][j]
            if word1[i] == word2[j]:
                return recur(word1, word2, i + 1, j + 1)

            dp[i][j] = 1 + min(recur(word1, word2, i + 1, j), recur(word1, word2, i, j + 1))

            return dp[i][j]

        return recur(word1, word2, 0, 0)
