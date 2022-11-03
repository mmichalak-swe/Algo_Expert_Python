# max Heap: O(k*log(n)) time | O(n) space
# max heap faster, still not as efficient as O(n) quicksort
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        
        for i in range(len(nums)):
            heapq.heappush(heap, -1*nums[i])
        
        for i in range(k-1):
            heapq.heappop(heap)
        
        return -1*heap[0]
