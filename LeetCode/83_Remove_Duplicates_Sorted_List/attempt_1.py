# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time | O(1) space
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         curr = head
        
#         while curr and curr.next:
#             nextPtr = curr.next
#             while curr.val == nextPtr.val:
#                 nextPtr = nextPtr.next
#                 if not nextPtr:
#                     break

#             curr.next = nextPtr
#             curr = curr.next

#         return head
    
        curr = head

        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next     # skip duplicated node
            curr = curr.next     # not duplicate of current node, move to next node

        return head
