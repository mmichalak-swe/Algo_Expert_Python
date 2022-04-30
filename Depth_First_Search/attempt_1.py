# O(V + E) Time | O(V) space
# where V is # of vertices, E is # of edges

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        
        if not array:
            array.append(self.name)
        
        for child in self.children:
            array.append(child.name)
            child.depthFirstSearch(array)
        
        return array
