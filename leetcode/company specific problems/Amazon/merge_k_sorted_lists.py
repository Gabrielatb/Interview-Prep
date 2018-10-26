#merge k sorted lists

class Node(object):
    """Creating Node in a Linked List """

    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.tail = new_node
      
def print_list(node):

    if node is None:
        return 'List is Empty'

    curr = node

    while curr:
        print curr.val
        curr = curr.next

# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

#brute force solution
#Time: O(nlogn)
#Space O(n)
    
# def merge_k_lsts(array_of_ll):

#     nodes = []
#     dummy = dummy_head = Node(0)
#     for ll in array_of_ll:
#         curr = ll.head
#         while curr:
#             nodes.append(curr.val)
#             curr = curr.next

    
#     for data in sorted(nodes):
#         new_node = Node(data)
#         dummy.next  = new_node
#         dummy = dummy.next
#     return print_list(dummy_head.next)



#Using priority queue
#Time: NK log K (push, pop takes log k times because need to heapify data structure)
#Space: O(k) heap wil have max of k elements at a time
from Queue import PriorityQueue

def merge_k_lsts(lists):
        
    dummy = dummy_head =  ListNode(0)
    q = PriorityQueue()

    for node in lists:
        if node:
            q.put(node.val, node)

    while q.qsize()>0:
        dummy.next = q.get()
        dummy = dummy.next
        if dummy.next:
            q.put((dummy.next.val, dummy.next))

    return dummy_head.next




        





if __name__ == '__main__':
    l1 = LinkedList()
    l1.append(1)
    l1.append(4)
    l1.append(7)
    l1.append(3)
    

    l2 = LinkedList()
    l2.append(5)
    l2.append(2)
    l2.append(9)
    l2.append(6)


    l3 = LinkedList()
    l3.append(8)
    l3.append(99)
    l3.append(10)
    l3.append(0)
    merge_k_lsts([l1, l2, l3])


# ***** Few Notes *********
# THE HEAPQ MODULE
# ****************

# This is a binary heap implementation usually backed by a plain list and it supports
#  insertion and extraction of the smallest element in O(log n) time.

# This module is a good choice for implementing priority queues in Python. 
# Because heapq technically only provides a min-heap implementation,
#  extra steps must be taken to ensure sort stability and other
#   features typically expected from a “practical” priority queue.


#  ************************
# THE QUEUE.PRIORITYQUEUE CLASS
#  ****************************
# This priority queue implementation uses
#  heapq internally and shares the same time and space complexities.

# The difference is that PriorityQueue is synchronized 
# and provides locking semantics to support multiple concurrent producers and consumers.

# Depending on your use case this might be helpful, or just incur unneeded overhead. 
# In any case you might prefer its class-based interface over using the function-based interface
#  provided by heapq.