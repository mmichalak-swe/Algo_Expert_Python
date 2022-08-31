# O(n) time | O(n) space, where n is the number of nodes
# Can be done in O(n) time, O(d) space, where d is the depth of the tree,
# to account for space on the call stack
def findMode(root):
    counts = {float('-inf'): 0}
    modeCount = float('-inf')
    output = []
    
    def recursiveHelper(root):
        if not root:
            return
        
        counts[root.val] = counts.get(root.val, 0) + 1
        
        if counts[root.val] > modeCount:
            modeCount = counts[root.val]
            output = [root.val]
        elif counts[root.val] == modeCount:
            output.append(root.val)
        
        recursiveHelper(root.left)
        recursiveHelper(root.right)
    
    recursiveHelper(root)
            
    return output
