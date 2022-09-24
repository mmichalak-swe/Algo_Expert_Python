# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n^2) time | O(h) space, n^2 to copy worst case valueStack to outputList
# O(h) space not counting output, to store call stack
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        valueStack = []
        outputList = []

        def recursiveHelper(node, targetSum, currentSum=0):
            if node is None:
                return
            
            valueStack.append(node.val)
            currentSum += node.val
            
            recursiveHelper(node.left, targetSum, currentSum)
            recursiveHelper(node.right, targetSum, currentSum)
            
            if currentSum == targetSum and node.left is None and node.right is None:
                outputList.append(valueStack[:])
        
            valueStack.pop()
        
        recursiveHelper(root, targetSum)
        
        return outputList
