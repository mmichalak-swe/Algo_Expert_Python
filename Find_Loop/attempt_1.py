# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Does NOT pass all test cases, brute force solution
# ~O(n) time, O(n) space
def findLoop(head):
    nodesVisited = []
    currNode = head

    while True:
        if currNode.value in nodesVisited:
            return currNode
        else:
            nodesVisited.append(currNode.value)
            currNode = currNode.next
