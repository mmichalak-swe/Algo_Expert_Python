# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n*log(k)) time | O(1) space, where k is the number of lists, and n is the length of the final list (worst case)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                
                mergedLists.append(self.mergeLists(list1, list2))
                
            lists = mergedLists
        
        return lists[0]
    
    def mergeLists(self, list1, list2):
        dummy = ListNode()
        ptr = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
            
        ptr.next = list1 if list1 else list2
        
        return dummy.next
