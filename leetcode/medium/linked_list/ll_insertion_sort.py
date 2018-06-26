# Sort a linked list using insertion sort.



class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        

        if head is None:
            return head
                
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        
        while curr.next:
            if curr.val > curr.next.val:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next
                    
                temp = curr.next
                curr.next = temp.next
                temp.next = pre.next
                pre.next = temp
                
                
            else:
                curr = curr.next
                
        return dummy.next

            