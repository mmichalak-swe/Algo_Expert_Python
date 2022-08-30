from collections import deque

# O(n) time | O(n) space, where n is the number of nodes
def levelOrder(root):
    if not root:
        return []

    output = []
    nodes = deque()
    nodes.append(root)
    
    while nodes:
        numNodes = len(nodes)
        output.append([])
        for i in range(numNodes):
            node = nodes.popleft()
            output[-1].append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
                
    return output
