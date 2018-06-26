# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        node = head
        prev = head

        while node.next and node.next.next:
            node = node.next.next
            prev = node.next

        l1 = self.sortList(prev.next)
        prev.next = None
        l2 = self.sortList(head)


        dummy = ListNode(0)
        ll = dummy

        while l1 and l2:
            if l1.val > l2.val:
                ll.next = l2
                l2 = l2.next
            else:
                ll.next = l1
                l1 = l1.next
            ll = ll.next

        if l1:
            ll.next = l1

        elif l2:
            ll.next = l2

        return dummy.next






