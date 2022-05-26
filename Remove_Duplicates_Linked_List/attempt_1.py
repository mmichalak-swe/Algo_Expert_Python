# O(n) time | O(1) space - where n is the number of nodes in the LL

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    node = linkedList

    while node.next is not None:

        if node.next.value == node.value:
            node.next = node.next.next
        else:
            node = node.next
    
    return linkedList
