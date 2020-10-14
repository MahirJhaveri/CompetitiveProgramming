# Problem 1171 - Remove Zero Sum Consecutive Nodes From Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        s = head.val
        node = head.next
        while s != 0 and node != None:
            s += node.val
            node = node.next
        if s == 0:
            return self.removeZeroSumSublists(node)
        elif head.next:
            head.next = self.removeZeroSumSublists(head.next)
            return head
        else:
            return head
