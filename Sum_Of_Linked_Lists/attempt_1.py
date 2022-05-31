# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    sumDigits = []

    node_one = linkedListOne
    node_two = linkedListTwo

    while node_one is not None or node_two is not None:
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
        sumDigits.append(sum)
    
    sumDigits = sumDigitsHelper(sumDigits)

    linkedListThree = LinkedList(sumDigits[0])
    currNode = linkedListThree
    
    for i in range(1, len(sumDigits)):
        currNode.next = LinkedList(sumDigits[i])
        currNode = currNode.next
        
    
    return linkedListThree


def sumDigitsHelper(array):
    for i in range(len(array)):
        if array[i] >= 10:
            try:
                array[i+1] += array[i] // 10
            except IndexError:
                array.append(array[i] // 10)
            array[i] -= 10
    return array
