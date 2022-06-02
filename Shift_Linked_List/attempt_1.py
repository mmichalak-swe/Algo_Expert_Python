# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def shiftLinkedList(head, k):
    length = 1
    currTail = head
    while currTail.next is not None:
        currTail = currTail.next
        length += 1

    offset = abs(k) % length
    if offset == 0:
        return head

    newTailIdx = length - offset if k > 0 else offset
    newTail = head
    for i in range(1, newTailIdx):
        newTail = newTail.next

    newHead = newTail.next
    newTail.next = None
    currTail.next = head

    return newHead
