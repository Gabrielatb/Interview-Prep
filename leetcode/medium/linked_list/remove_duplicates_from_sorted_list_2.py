# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Example 1:

# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:

# Input: 1->1->1->2->3
# Output: 2->3


def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev, curr = dummy, dummy.next
    
    while curr:
        if curr.next and curr.next.val == curr.val:
            rem = curr.val
            
            while curr and curr.val == rem:
                curr = curr.next
                
            prev.next = curr
            
        else:
            prev, curr = curr, curr.next
            
    return dummy.next
                    
                