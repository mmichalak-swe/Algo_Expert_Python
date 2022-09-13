# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time | O(1) space
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        oneBack = None
        slow = head
        fast = head.next
        
        while fast and fast.next:
            oneBack = slow
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow.next = slow.next.next
        else:
            oneBack.next = slow.next

        return head
