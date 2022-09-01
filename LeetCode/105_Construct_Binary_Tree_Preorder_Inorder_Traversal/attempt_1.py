# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i

        def recursiveHelper(preorder, inorder):
            if not preorder or not inorder:
                return

            root = TreeNode(preorder[0])
            idx = map_inorder[preorder[0]] # O(1)
            root.left = self.buildTree(preorder[1:idx+1], inorder[:idx]) # O(n)
            root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:]) # O(n)

            return root
        
        return recursiveHelper(preorder, inorder)
