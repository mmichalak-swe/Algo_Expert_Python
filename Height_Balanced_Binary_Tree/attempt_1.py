# O(n) time | O(h) space where n is # nodes in the tree

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height


def height_balanced_binary_tree(tree):
    tree_info = get_tree_info(tree)
    return tree_info.is_balanced


def get_tree_info(node):
    if node is None:
        return TreeInfo(True, -1)

    left_subtree_info = get_tree_info(node.left)
    right_subtree_info = get_tree_info(node.right)

    is_balanced = (
        left_subtree_info.is_balanced
        and right_subtree_info.is_balanced
        and abs(left_subtree_info.height - right_subtree_info.height) <= 1
    )

    height = max(left_subtree_info.height, right_subtree_info.height) + 1

    return TreeInfo(is_balanced, height)
