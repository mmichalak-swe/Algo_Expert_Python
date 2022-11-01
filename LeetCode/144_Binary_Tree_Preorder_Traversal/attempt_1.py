# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Solution
# O(n) time | O(h) space
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
        
        def helper(node):
            if not node:
                return
            
            output.append(node.val)
            
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return output
