# O(n*log(d)) time | O(1) space, where n is the len of bloomDays,
# and d is the difference between the max of bloomDays, and the min
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < k * m:
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            currentDay = (left + right) // 2
            bouquetsMade = 0
            adjacentCount = 0

            for i, day in enumerate(bloomDay):
                if day <= currentDay:
                    adjacentCount += 1
                    if adjacentCount == k:
                        bouquetsMade += 1
                        adjacentCount = 0
                else:
                    adjacentCount = 0

            if bouquetsMade < m:
                left = currentDay + 1
            else:
                right = currentDay

        return right
