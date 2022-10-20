# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(h) space
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        output = []
        
        def dfs(node, path):
            if not node:
                return
            
            path.append(str(node.val))
            
            if not node.left and not node.right:
                output.append('->'.join(path))
                # can do without the next two lines, minor efficiency improvement
                path.pop()
                return
            
            dfs(node.left, path)
            dfs(node.right, path)
            
            path.pop()
        
        dfs(root, [])
        
        return output
