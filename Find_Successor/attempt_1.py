# O(n) time | O(n) space

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
	
	result = findSuccessorHelper(tree)
	
	# if result.index(node) < len(result) - 1:
	# 	return result[result.index(node) + 1]
	# else:
	# 	return None
	
	try:
		return result[result.index(node) + 1]
	except (ValueError, IndexError):
		return None

    
def findSuccessorHelper(curr_node, traversal_list=[]):
    if not curr_node:
        return traversal_list
    
    findSuccessorHelper(curr_node.left, traversal_list)
    traversal_list.append(curr_node)
    findSuccessorHelper(curr_node.right, traversal_list)
    
    return traversal_list

