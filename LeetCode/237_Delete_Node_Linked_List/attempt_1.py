# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(1) time | O(1) space
# Copy next node val to current node,
# set currNode.next to two nodes away (original next node of node after deleted node)
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val = node.next.val
        node.next = node.next.next
