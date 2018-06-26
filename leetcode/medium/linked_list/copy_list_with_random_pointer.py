# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.




class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if head is None:
            return None
        
        nodes_dict = {}
        node = head
        
        while node:
            nodes_dict[node] = RandomListNode(node.label)
            node = node.next
            
        node = head
        while node:
            nodes_dict[node].next = nodes_dict[node.next] if node.next else None
            nodes_dict[node].random = nodes_dict[node.random] if node.random else None
            node = node.next
            
        return nodes_dict[head]