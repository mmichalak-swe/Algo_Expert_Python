# min Heap: O(n*log(k)) time | O(k) space
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        
        for i in range(len(nums)):
            if len(heap) < k:
                heapq.heappush(heap, nums[i])
            else:
                if nums[i] > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, nums[i])
        
        return heap[0]
