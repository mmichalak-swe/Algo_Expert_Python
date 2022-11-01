import heapq

# O(n*log(k)) time | O(n) space
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        h = []
        table = {}
        
        for word in words:
            table[word] = 1 + table.get(word, 0)
        
        for word in table:
            heapq.heappush(h, (-1*table[word], word))

        return [heapq.heappop(h)[1] for i in range(k)]
