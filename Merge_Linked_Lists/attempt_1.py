# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n + m) time | O(1) space where n is # of nodes in first list, m is #
# of nodes in second list
def mergeLinkedLists(headOne, headTwo):
    nodeInTwo = headTwo
    prev = None
    curr = headOne
    
    while nodeInTwo is not None:
        if curr is None:
            prev.next = nodeInTwo
            break

        if nodeInTwo.value < curr.value:
            if prev is None:
                temp_head = LinkedList(headTwo.value)
                temp_list = headOne
                headOne = temp_head
                headOne.next = temp_list
                prev = headOne
                curr = headOne.next
                nodeInTwo = nodeInTwo.next
                continue
            else:
                temp_node = LinkedList(nodeInTwo.value)
                prev.next = temp_node
                temp_node.next = curr
                prev = prev.next
                nodeInTwo = nodeInTwo.next
        else:
            prev = curr
            curr = curr.next

    return headOne
