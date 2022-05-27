# O(n) time | O(1) space

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    first_ptr = head
    second_ptr = head
    counter = 1

    while counter <= k:
        second_ptr = second_ptr.next
        counter += 1

    if second_ptr is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    while second_ptr.next is not None:
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next
    first_ptr.next = first_ptr.next.next
