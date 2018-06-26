# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Example:

# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = beg = ListNode(0)
        h2 = end = ListNode(0)

        while head:
            if head.val < x:
                beg.next = head
                beg = beg.next
            else:
                end.next = head
                end = end.next
                
            head = head.next
                
        beg.next = h2.next
        end.next = None
        
        return h1.next
                