class Solution:
    # O(n * m) time | O(2m) space
    # only store 2 rows vs the entire grid, space optimized
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1:
            return 1

        table = [[1] * n]   # Initial first row of all 1's
        table[0].append(0)  # Add 0 to end for DP solution
        table.append([0] * (n + 1)) # Initial bottom row of 0's for DP solution

        for row in reversed(range(m)):
            for col in reversed(range(n)):
                if col == n - 1:
                    table[0][col] = 1
                else:
                    table[0][col] = table[0][col + 1] + table[1][col]
            table[1] = table[0][:]
            
        return table[0][0]
