# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time | O(1) space
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        odd = head       # ptr that moves through odd list to skip even nodes
        p2 = head.next   # ptr that remains at head of even list (second node in list)
        even = head.next # ptr that moves through even list to skip odd nodes
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        # link end of odd list to start of even list
        odd.next = p2
        
        return head
