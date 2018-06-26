# Given a linked list, swap every two adjacent nodes and return its head.

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Note:

# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.


def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    
    while current.next and current.next.next:
        temp = current.next.next
        current.next.next = temp.next
        temp.next = current.next
        current.next = temp
        current = current.next.next
        
    return dummy.next
