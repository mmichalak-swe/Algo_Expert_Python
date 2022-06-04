# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    def breadthFirstSearch(self, array):
        queue = []
        queue.append(self)
        while len(queue) > 0:
            currNode = queue.pop(0)
            for child in currNode.children:
                queue.append(child)
            array.append(currNode.name)
        return array
