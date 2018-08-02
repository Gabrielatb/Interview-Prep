#write code to partition a linked list around a value, all nodes less than value 
#come before all nodes greater than or equal to the value


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        curr = head
        
        while curr:
            if curr.val < x:
                l1.next = curr
                l1 = l1.next
            else:
                l2.next = curr
                l2 = l2.next
            curr = curr.next
            
        l2.next = None
        l1.next = h2.next
        return h1.next