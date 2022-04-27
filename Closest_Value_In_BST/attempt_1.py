# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space

def findClosestValueInBst(tree, target):

    curr_node = tree
    closest_to_target = curr_node.value
    
    while curr_node:
        delta = abs(target - curr_node.value)
        if delta < abs(target - closest_to_target):
            closest_to_target = curr_node.value
    
        if target > curr_node.value:
            curr_node = curr_node.right
        elif target < curr_node.value:
            curr_node = curr_node.left
        else:
            break

    return closest_to_target
    
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
