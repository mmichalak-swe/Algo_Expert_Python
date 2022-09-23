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
        
        while curr:
            while curr.next and curr.next.val == curr.val:
                before.next = before.next.next
                curr = curr.next
                
                if not curr.next or curr.next.val != curr.val:
                    before.next = before.next.next
                    curr = curr.next
                    
                    if not curr:
                        break
                        
            if not curr:
                break
                        
            curr = curr.next
            before = before.next
        
        return dummy.next
