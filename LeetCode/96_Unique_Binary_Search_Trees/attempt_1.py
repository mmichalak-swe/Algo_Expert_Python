# O(n^2) time | O(n) space
class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}

        def recurse(n):
          if n in memo:
            return memo[n]

          if n == 0:
            return 1

          total = 0
          for j in range(1, n + 1):
            left = recurse(j - 1)
            right = recurse(n - j)
            total += right * left
          memo[n] = total
          return total

        return recurse(n)
