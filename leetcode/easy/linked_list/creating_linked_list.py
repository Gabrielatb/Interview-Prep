# Iplementation of basic insertion and traversal of a linked list. From mycodeschool, in addition to other functions I have added


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
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = node
        self.tail = node


    def append_beg(self, data):
        node = Node(data)

        if self.head is None:
            print "inside self.head is None"
            self.head = node
        else:
            print "inside self.head is not None"
            dummy = self.head
            self.head = node
            self.head.next = dummy



    def print_list(self):
        current = self.head

        while current is not None:
            print current.val
            current = current.next

    def find(self, data):
        current = self.head
        while current is not None:
            if current.val == data:
                return data + " is in your Linekd List"
            else:
                current = current.next
        return data + ' is not in your Linked list'



    def remove(self, value):
        if self.head is not None and self.head.val == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return 

        current = self.head

        while current.next is not None:
            if current.next.val == value:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return

            current = current.next


        


class LinkedListNoTail(object):

    def __init__(self):
        self.head = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = node


    def print_list(self):

        current = self.head

        while current is not None:
            print current.val
            current = current.next




if __name__ == '__main__':
    # ll_no_tail = LinkedListNoTail()
    # ll_no_tail.append_node('apple')
    # ll_no_tail.append_node('berry')
    # ll_no_tail.append_node('cherry')

    linked_list = LinkedList()
    linked_list.append_end('apple')
    linked_list.append_end('berry')
    linked_list.append_end('cherry')




