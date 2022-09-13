# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n + m) time | O(n + m) space, where n is the len of one input list, m is the len of the other
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None
        
        # Puts base node of value 0 to make rest of code easier, return .next of this dummy node
        output = currNode = ListNode(0)
        while list1 or list2:
            if not list1:
                currNode.next = ListNode(list2.val)
                list2 = list2.next
            elif not list2:
                currNode.next = ListNode(list1.val)
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    currNode.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    currNode.next = ListNode(list2.val)
                    list2 = list2.next

            currNode = currNode.next
    
        return output.next
