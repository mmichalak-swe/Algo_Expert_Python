# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i
        
        # O(n^2) time | O(n^2) space (recursive calls and slices)
        def recursiveHelper(inorder, postorder):
            if not inorder or not postorder:
                return

            root = TreeNode(postorder.pop())
            print(root.val)
            idx = map_inorder[root.val] # O(1)

            root.right = self.buildTree(inorder[idx + 1:], postorder[idx:]) # O(n)
            root.left = self.buildTree(inorder[:idx], postorder[:idx]) # O(n)

            return root
        
        return recursiveHelper(inorder, postorder)

# O(n) time | O(1) space
# class Solution:
#     def buildTree(self, inorder, postorder):
#         map_inorder = {}
#         for i, val in enumerate(inorder): map_inorder[val] = i
#         def recur(low, high):
#             if low > high: return None
#             x = TreeNode(postorder.pop())
#             mid = map_inorder[x.val]
#             x.right = recur(mid+1, high)
#             x.left = recur(low, mid-1)
#             return x
#         return recur(0, len(inorder)-1)
