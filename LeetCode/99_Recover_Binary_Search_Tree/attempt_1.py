# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(h) space
# worst case O(h) space due to recursive call stack
class Solution:
    first = None
    second = None
    prev = TreeNode(float('-inf'))

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def inOrder(node):
            if not node:
                return
            
            inOrder(node.left)
            
            # If first element not assigned, assign to prev
            if not self.first and self.prev.val >= node.val:
                self.first = self.prev
            
            # If first element found, assign second element to node
            if self.first and self.prev.val >= node.val:
                self.second = node
            
            self.prev = node
            
            inOrder(node.right)

        inOrder(root)
        
        tempVal = self.first.val
        self.first.val, self.second.val = self.second.val, self.first.val
        return root
