#write code to remove duplicates from an unsorted linked list

class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):

        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node

        elif self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def print_list(self):

        curr = self.head

        while curr:
            print curr.val
            curr = curr.next

    def remove_dups(self):

        curr = self.head

        while curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return self.print_list()











if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(3)
    ll.append(3)
    ll.append(4)
    ll.append(4)
