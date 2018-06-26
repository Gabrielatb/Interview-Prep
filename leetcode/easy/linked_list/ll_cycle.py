# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
#space complexity O(n)
        visited_nodes = []
        current = head
        
        while current:
            if current in visited_nodes:
                return True
            else:
                visited_nodes.append(current)
                current = current.next
        return False
        
    
    #space  complexity O(1)
        if head is None:
            return False
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
                
            if slow == fast:
                return True
                
        return False
    # linked_list.append(four)