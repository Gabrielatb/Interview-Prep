#Input is a doubly linked list of sorted numbers 
#Return is height balanced BST



 def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def find_mid(head):
            prev = ListNode(0)
            fast, slow = head, head
            prev.next = slow
            
            while fast and fast.next:
                prev = prev.next
                slow = slow.next
                fast = fast.next.next
                
            prev.next = None
            return slow
        
        curr = head
        if curr is None:
            return None
        if curr.next is None:
            return TreeNode(curr.val)
     
       
        mid = find_mid(curr)
        
        node = TreeNode(mid.val)
        node.left = self.sortedListToBST(curr)
        node.right = self.sortedListToBST(mid.next)
        
        return node
        
        
        