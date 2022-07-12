# SAME BIG O FOR ALL THREE
# O(n) time | O(n) space, where n is the # of nodes in the BST
def inOrderTraverse(tree, array):
    if tree is None:
        return

    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    if tree is None:
        return

    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree is None:
        return

    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)
    return array
