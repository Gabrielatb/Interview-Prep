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

    def print_list(self):

        current = self.head

        while current is not None:
            print current.val
            current = current.next

#quick sort
#Time Complexity: O(nlogn)
#Space Complexity: ()



if __name__ == '__main__':
    ll = LinkedList()
    ll.append(4)
    ll.append(3)
    ll.append(2)
    ll.append(1)

    quicksort(ll.head)
