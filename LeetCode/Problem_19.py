class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        ptr1 = head
        ptr2 = head
        
        i=0
        while i<n:
            ptr1 = ptr1.next
            i+=1
        
        while ptr1 != None and ptr1.next != None:
            ptr2 = ptr2.next
            ptr1=ptr1.next
        
        if ptr1 == None:
            return head.next
        ptr2.next = ptr2.next.next
        
        return head
        
