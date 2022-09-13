# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time | O(1) space
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return head
        
        # Make second half of list a separate list, reverse it
        slow = head
        fast = slow.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalf = slow.next
        slow.next = None
        
        # Reverse from slow.next to end
        prev, curr = None, secondHalf
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        reverse = prev
        curr = head

        while reverse:
            currTemp = curr.next
            reverseTemp = reverse.next
            
            reverse.next = currTemp
            curr.next = reverse
            curr = curr.next.next
            
            reverse = reverseTemp
