# # Sort a linked list in O(n log n) time using constant space complexity.

# # Example 1:

# # Input: 4->2->1->3
# # Output: 1->2->3->4
# # Example 2:

# # Input: -1->5->3->4->0
# # Output: -1->0->3->4->5


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        mid = head
        fast = head
        while fast.next and fast.next.next:
            mid = mid.next
            fast = fast.next.next

        left_ll = mid.next
        left = self.sortList(left_ll)
        mid.next = None
        right = self.sortList(head)

        

            
        



