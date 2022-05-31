# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def reverseLinkedList(head):
    firstNode = head if head is not None else None

    if firstNode is None:
        return None
    if firstNode.next is None:
        return firstNode
    
    secondNode = firstNode.next

    if secondNode.next is None:
        secondNode.next = firstNode
        firstNode.next = None
        return secondNode

    thirdNode = secondNode.next
    
    while True:
        secondNode.next = firstNode
        if thirdNode is None:
            return secondNode
        if firstNode == head:
            firstNode.next = None
        firstNode = secondNode
        secondNode = thirdNode
        thirdNode = thirdNode.next
