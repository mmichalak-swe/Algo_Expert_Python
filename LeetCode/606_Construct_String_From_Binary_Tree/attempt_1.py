# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(n) space, where n is the number of nodes
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        output = []
        
        def recursiveHelper(root):
            if not root:
                return
            
            output.append("(")
            output.append(str(root.val))
            
            if root.left and root.right:
                recursiveHelper(root.left)
                recursiveHelper(root.right)
            elif root.left and not root.right:
                recursiveHelper(root.left)
            elif root.right and not root.left:
                output.append("()")
                recursiveHelper(root.right)
            
            output.append(")")
        
        recursiveHelper(root)
        
        return ''.join(output)[1:-1]
