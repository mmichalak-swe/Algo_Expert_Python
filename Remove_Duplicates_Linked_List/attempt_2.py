# O(n) time | O(1) space - where n is the number of nodes in the LL

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    node = linkedList

    while node is not None:
        next_unique = node.next

        while next_unique and next_unique.value == node.value:
            next_unique = next_unique.next

        node.next = next_unique
        node = next_unique
            
    
    return linkedList
