"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# O(n) time | O(n) space
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []

        def recursiveHelper(node):
            if not node:
                return

            output.append(node.val)
            
            for child in node.children:
                recursiveHelper(child)

        recursiveHelper(root)
        return output
