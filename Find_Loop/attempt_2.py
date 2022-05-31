# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space
def findLoop(head):
    first_ptr = head.next
    second_ptr = head.next.next

    while first_ptr != second_ptr:
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next.next

    first_ptr = head

    while first_ptr != second_ptr:
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next

    return first_ptr
