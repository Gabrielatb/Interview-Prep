# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example 1:

# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:

# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        
        while head is None:
            return head
        
        neg = -1
        pos = 1
        dummy = ListNode(0)
        dummy.next = head
        res = dummy.next
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        head = dummy.next
        for i in range(len(nums)):
            if i ==0:
                continue
            if i % 2 == 0:
                head.next = ListNode(nums[pos])
                pos +=1
                head = head.next
                
            else:
                head.next = ListNode(nums[neg])
                neg -= 1
                head = head.next
                
        head.next = None
        
        