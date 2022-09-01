"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # O(v + e) time | O(v) space
    def cloneGraph(self, node: 'Node') -> 'Node':
        neighborhood = {} # O(v) space
        
        def recursiveHelper(node):
            if node in neighborhood:
                return neighborhood[node]

            newNode = Node(node.val)
            neighborhood[node] = newNode
                
            for neighbor in node.neighbors:
                newNode.neighbors.append(recursiveHelper(neighbor))

            return newNode
        
        return recursiveHelper(node) if node else None
