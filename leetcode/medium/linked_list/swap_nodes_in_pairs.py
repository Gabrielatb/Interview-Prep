# Given a linked list, swap every two adjacent nodes and return its head.

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Note:

# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.


class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

        self.tail = new_node

    def swap(self):

        if self.head is None or self.head.next is None:
            return head
 
        dummy = dummy_head = ListNode(0)
        
        first = self.head
        second = self.head.next
        
        # while first and second:
        temp = second
        second = first
        first = temp
        print first.data
        print first.next.data
            # dummy.next = second
            # print second.data
            # print dummy.next.data
            
            # first = first.next
            # second = second.next

      
            
            




if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)



























# def swapPairs(self, head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
#     dummy = ListNode(0)
#     dummy.next = head
#     current = dummy
    
    
#     while current.next and current.next.next:
#         temp = current.next.next
#         current.next.next = temp.next
#         temp.next = current.next
#         current.next = temp
#         current = current.next.next
        
#     return dummy.next
