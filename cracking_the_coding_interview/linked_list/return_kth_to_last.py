# return kth to last element of a singly linked list


class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    """Linked List using head and tail.

    Let's make a list:

        >>> ll = LinkedList()

        >>> ll.print_list()

        >>> ll.append(1)
        >>> ll.append(2)
        >>> ll.append(3)
        >>> ll.append(4)
        >>> ll.append(5)
        >>> ll.append(6)
        >>> ll.append(7)

        >>> ll.print_list()
        1
        2
        3
        4
        5
        6
        7

    # Test return_k_last(2):

    #     >>> ll.return_k_last(2)
    #     5

    """


    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, data):

        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node

        else:
            self.tail.next = new_node

        self.tail = new_node

    def print_list(self):
        curr = self.head

        while curr:
            print curr.data
            curr = curr.next


    def return_k_last(self, k):

        res_pointer = end_pointer = self.head

        for _ in range(k):
            end_pointer = end_pointer.next

        while end_pointer:
            end_pointer = end_pointer.next
            res_pointer= res_pointer.next

        return res_pointer.data

    def delete_k_last(self, k):

        dummy = ListNode(0)
        dummy.next = head
        res_pointer, end_pointer = dummy, dummy
        
        for _ in range(k):
            end_pointer = end_pointer.next
            
        while end_pointer and end_pointer.next:
            res_pointer = res_pointer.next
            end_pointer = end_pointer.next
            
        res_pointer.next = res_pointer.next.next
            
        return dummy.next








if __name__ == "__main__":
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)







