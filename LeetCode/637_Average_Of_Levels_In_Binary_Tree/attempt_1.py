# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# O(n) time | O(n) space, where n is the number of nodes in the tree
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        nodes = deque()
        nodes.append(root)
        
        output = []
        
        while nodes:
            sum = 0
            count = 0
            for i in range(len(nodes)):
                current = nodes.popleft()
                
                if current.left:
                    nodes.append(current.left)
                if current.right:
                    nodes.append(current.right)
                
                sum += current.val
                count += 1
            
            output.append(sum/count)
        
        return output
