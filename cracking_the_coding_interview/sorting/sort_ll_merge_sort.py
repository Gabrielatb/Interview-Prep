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
        
        middle_node = self.find_middle_node(head)
        right  = middle_node.next
        middle_node.next = None
        return self.merge_sort(self.sortList(head), self.sortList(right))
        
        
    def find_middle_node(self, head):
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
    def merge_sort(self, head1, head2):
        dummy = node = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next
            
        node.next = head1 or head2
            
        return dummy.next 