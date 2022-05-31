# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(max(n,m)) time | O(max(n,m)) space - where n and m are the length of
# LL one and LL two
def sumOfLinkedLists(linkedListOne, linkedListTwo):

    node_one = linkedListOne
    node_two = linkedListTwo

    linkedListThree = LinkedList(0)
    currNode = linkedListThree
    carryover = 0

    while node_one is not None or node_two is not None or carryover != 0:
        sum = 0
        try:
            sum += node_one.value
            node_one = node_one.next
        except:
            sum += 0
        try:
            sum += node_two.value
            node_two = node_two.next
        except:
            sum += 0
        
        sum += carryover

        if sum >= 10:
            carryover = sum // 10
            sum %= 10
        else:
            carryover = 0

        newNode = LinkedList(sum)
        currNode.next = newNode
        currNode = currNode.next

    return linkedListThree.next
