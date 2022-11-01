# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n*log(n)) time | O(n) space
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        values = []
        
        while node is not None:
            values.append(node.val)
            node = node.next
        
        values.sort()
        dummy = ListNode(0)
        output = dummy
        
        for value in values:
            dummy.next = ListNode(value)
            dummy = dummy.next
        
        return output.next
