def isValidBST(self, root):
    
    def recursiveHelper(root, minVal=float('-inf'), maxVal=float('inf')):
        if not root:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        
        return recursiveHelper(root.left, minVal, root.val) and recursiveHelper(root.right, root.val, maxVal)
    
    return recursiveHelper(root)
