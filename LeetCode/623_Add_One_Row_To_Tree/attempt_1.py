# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(h) space, where n is the number of nodes, and h is the height of the tree
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        
        def dfs(node, prev, way, d):
            # if not node:
            #     if d == depth:
            #         newNode = TreeNode(val)
            #         if way == "left":
            #             prev.left = newNode
            #         else:
            #             prev.right = newNode
            #     return
            
            if d == depth:
                newNode = TreeNode(val)
                if way == "left":
                    newNode.left = prev.left
                    prev.left = newNode
                else:
                    newNode.right = prev.right
                    prev.right = newNode
                return
            
            if not node:
                return
            
            dfs(node.left, node, "left", d+1)
            dfs(node.right, node, "right", d+1)
        

        dfs(root, None, None, 1)        
        return root
