# Problem 25 - Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# identify the first k nodes,
# then recurse on the rem,
# then reverse the first k nodes

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        node = head
        while node != None and count < k:
            node = node.next
            count += 1
        if count < k:
            return head
        node = self.reverseKGroup(node, k)
        
        count = 0
        while count < k:
            temp = head.next
            head.next = node
            node = head
            head = temp
            count += 1
        return node
            
        
