import heapq
# O(n*log(n)) time | O(n) space, where n is the number of stones
# n*log(n) time because heap pop takes log(n), a max of n times in this case
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            
            if stone1 < stone2:
                heapq.heappush(stones, stone1 - stone2)

        stones.append(0)
        return stones[0] * -1
