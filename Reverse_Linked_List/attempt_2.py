# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def reverseLinkedList(head):
    previous, current = None, head
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous
