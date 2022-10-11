# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n*log(n)) time | O(n) space
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        values = []
        
        while node is not None:
            values.append(node.val)
            node = node.next
        
        values.sort()
        node = head
        
        for value in values:
            node.val = value
            node = node.next

        return head
