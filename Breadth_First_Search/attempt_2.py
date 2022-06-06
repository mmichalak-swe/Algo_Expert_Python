from collections import deque

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
        q = deque()
        q.append(self)
        while len(q) > 0:
            currNode = q.popleft()
            array.append(currNode.name)
            for child in currNode.children:
                q.append(child)
        return array
