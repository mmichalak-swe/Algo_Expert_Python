# Recursive Solution
# O(n) time | O(n + log(n)) space, where n is the number of nodes
# O(n) space for output list, O(log(n)) space for max recursive call stack
def inorderTraversal(root):
        
    output = []

    def recursiveHelper(root):
        if not root:
            return

        recursiveHelper(root.left)
        output.append(root.val)
        recursiveHelper(root.right)

    recursiveHelper(root)

    return output

# Iterative Solution
# O(n) time | O(n) space, where n is the number of nodes
def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
