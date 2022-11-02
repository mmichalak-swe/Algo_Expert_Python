# O(n^2) time | O(n) space
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = [(start, 0)]
        visited = set(start)
        
        while queue:
            current, changes = queue.pop()
            if current == end:
                return changes
            
            for gene in bank:
                if gene in visited:
                    continue
            
                diff = 0
                for idx in range(len(current)):
                    if current[idx] != gene[idx]:
                        diff += 1
                
                if diff == 1 and gene not in visited:
                    queue.append((gene, changes + 1))
                    visited.add(gene)
        
        return -1
