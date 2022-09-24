# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n) time | O(1) space
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return None

        slow = head.next
        fast = head.next.next
        
        while fast and slow != fast:
            if fast.next: # if not fast.next, at last node of list, no cycle
                slow = slow.next
                fast = fast.next.next
            else:
                return None
        
        # past last node of list, no cycle
        if not fast:
            return None
        
        p1 = head
        
        while p1 != fast:
            p1 = p1.next
            fast = fast.next

        return p1
