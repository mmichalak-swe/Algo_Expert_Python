# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(h) space
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(node):
            if not node:
                return
            
            node.left, node.right = node.right, node.left
            
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return root
