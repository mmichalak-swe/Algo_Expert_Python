# O(n) time | O(1) space
class Solution:
    secondMin = None
    
    def findSecondMinimumValue(self, root):
        self.secondMin = float('inf')
        highestNodeVal = root.val
        
        def recursiveHelper(root):
            if not root:
                return
            if root.val > self.secondMin:
                return
            
            recursiveHelper(root.right)
            
            if highestNodeVal < root.val < self.secondMin:
                self.secondMin = root.val
            
            recursiveHelper(root.left)

        recursiveHelper(root)

        return self.secondMin if self.secondMin != float('inf') else -1
