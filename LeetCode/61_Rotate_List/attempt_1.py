# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time | O(1) space
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        lastNode = head
        length = 1
        
        # get the length of the list and the last node in the list
        while lastNode.next:
            lastNode = lastNode.next
            length += 1
        
        # modify k to be less than length
        k %= length

        # connect lastNode to head to create circular linked list
        lastNode.next = head
        
        # traverse to 1 before kth node from end
        temp = head
        for i in range(length - k - 1):
            temp = temp.next
        
        # break circular link, return ans
        ans = temp.next
        temp.next = None
        
        return ans
