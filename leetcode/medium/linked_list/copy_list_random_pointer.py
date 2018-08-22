# A linked list is given such that each node contains an additional random 
#pointer which could point to any node in the list or null.

# Return a deep copy of the list.


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        ll_dict = {}

        curr = head
        while curr:
            ll_dict[curr] = RandomListNode(curr.label)
            curr = curr.next

        curr = head
        while curr:
            ll_dict[curr].next = ll_dict[curr.next] if curr.next else None
            ll_dict[curr].random = ll_dict[curr.random] if curr.random else None
            curr = curr.next

        return ll_dict[head] if head else None