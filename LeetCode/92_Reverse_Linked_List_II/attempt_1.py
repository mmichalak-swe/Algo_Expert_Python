# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time | O(1) space, where n is the num of nodes in the input list
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(0, head)
        curr = head
        before = dummy
        
        # move before, curr to correct spot to start reverse
        for i in range(left - 1):
            before = curr
            curr = curr.next
        
        # reverse correct section of list
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # link new end of list to rest of list after reverse
        before.next.next = curr
        
        # link start of list to reversed portion
        before.next = prev
        
        return dummy.next
