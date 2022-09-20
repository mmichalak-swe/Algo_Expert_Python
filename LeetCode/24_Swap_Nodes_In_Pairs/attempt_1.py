# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time | O(1) space
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = ListNode(0, head)
        prevPtr = prev
        
        while node and node.next:
            restOfList = node.next.next
            
            newSecond, newFirst = node, node.next
            newSecond.next = restOfList
            newFirst.next = newSecond
            
            prevPtr.next = newFirst
            prevPtr = newSecond
            node = prevPtr.next
        
        return prev.next
