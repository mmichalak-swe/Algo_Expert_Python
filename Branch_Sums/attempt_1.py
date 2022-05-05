# O(n) time | O(n) space - n is # of nodes in tree

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    ans = []
    calcBranchSums(root, 0, ans)
    return ans

def calcBranchSums(node, running_sum, curr_sum):
    if not node:
        return
    
    new_running_sum = running_sum + node.value
    
    if not node.left and not node.right:
        curr_sum.append(new_running_sum)
        return
    
    calcBranchSums(node.left, new_running_sum, curr_sum)
    calcBranchSums(node.right, new_running_sum, curr_sum)
