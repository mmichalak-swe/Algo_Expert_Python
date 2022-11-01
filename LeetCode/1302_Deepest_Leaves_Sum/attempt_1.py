# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(h) space, where n is the number of nodes,
# and h is the height of the tree (recursive call stack)
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def depthFinder(node):
            if not node:
                return 0
            
            return max(1 + depthFinder(node.left), 1 + depthFinder(node.right))
        
        maxDepth = depthFinder(root)
        
        def sumCalc(node, depth, maxDepth):
            if not node:
                return 0
            
            if depth == maxDepth:
                return node.val
            
            return sumCalc(node.left, depth+1, maxDepth) + sumCalc(node.right, depth+1, maxDepth)
        
        return sumCalc(root, 1, maxDepth)
