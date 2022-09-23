# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time | O(1) space
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        before = dummy
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.next and curr.next.val == curr.val:
                    curr = curr.next
                curr = curr.next
                before.next = curr
                
            else:
                before = before.next
                curr = curr.next
        
        return dummy.next
