# O(n*log(max(piles))) time | O(1) space
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            speed = (left + right) // 2
            if sum(math.ceil(p/speed) for p in piles) > h:
                left = speed + 1
            else:
                right = speed

        return left
