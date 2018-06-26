# Reverse a linked list from position m to n. Do it in one-pass.

# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:

# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL



def reverseBetween(self, head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head

    m_point = dummy


    for _ in range(m-1):
        m_point = m_point.next
        
    current = m_point.next
    prev = None
    for _ in range(n-m +1 ):
        next_element = current.next
        current.next = prev
        prev = current
        current = next_element
      


    m_point.next.next = current
    m_point.next = prev

    return dummy.next
                