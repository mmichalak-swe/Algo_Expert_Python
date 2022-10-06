# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(n) space, where n is the number of nodes
# note: O(h) space for recursive calls on call stack
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
        
        def post(node):
            if not node:
                return
            
            post(node.left)
            post(node.right)
            
            output.append(node.val)
        
        post(root)
        return output
