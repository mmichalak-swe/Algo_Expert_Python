# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n^2) time | O(h) space, n^2 to copy worst case path to outputList
# O(h) space not counting output, to store call stack
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        outputList = []

        def recursiveHelper(node, targetSum, path=[]):
            if node is None:
                return
            
            path.append(node.val)
            targetSum -= node.val
            
            if targetSum == 0 and node.left is None and node.right is None:
                outputList.append(path[:])
            
            recursiveHelper(node.left, targetSum, path)
            recursiveHelper(node.right, targetSum, path)
            
            path.pop()

            
        recursiveHelper(root, targetSum)
        return outputList
