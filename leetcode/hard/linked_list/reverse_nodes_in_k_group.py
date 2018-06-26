# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Example:

# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

# Note:

# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.


class Solution(object):
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            #newhead, #newtail
        return prev, head
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        dummy = ListNode(0)
        dummy.next = head
        to_new_head = dummy
        
        while to_new_head and to_new_head.next:
            tail = to_new_head
            for _ in range(k):
                tail = tail.next
                if tail is None:
                    to_new_head = None
                    break
            else:
                from_new_tail = tail.next
                tail.next = None
                new_head, new_tail = self.reverse(to_new_head.next)
                to_new_head.next = new_head
                new_tail.next = from_new_tail
                to_new_head = new_tail
                    
                    
                    
        return dummy.next





