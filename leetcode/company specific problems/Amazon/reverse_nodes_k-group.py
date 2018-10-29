# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Example:

# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5


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
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = new_node
        self.tail = new_node

    def print_list(self):
        if self.head is None:
            return 'Nothing to print'

        current = self.head

        while current is not None:
            print current.val
            current = current.next
        return

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        def reverse(curr):
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
  
            
        dummy = dummy_head = Node(0)
        curr = head
        while curr:
            curr_head = curr
            for _ in range(k-1):
                if curr.next is None:
                    dummy.next = curr_head
                    return dummy_head.next
                else:
                    curr = curr.next
                
            temp = curr.next
            curr.next = None
            curr = temp
            new_head = reverse(curr_head)
            dummy.next = new_head
            while dummy.next:
                dummy = dummy.next

        print dummy_head.next


            
            
            


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    # print linked_list.print_list()
    print linked_list.reverseKGroup(linked_list.head, 3)
    linked_list.print_list()
