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

    def quicksort_ll(head):

        if head is None or head.next is None:
            return None

        pivot = find_mid(head)
        left = left_head = Node(0)
        right = right_head = Node(0)
        eq = eq_head = Node(0)

        curr = head
        while curr:
            if curr.val > pivot.val:
                right.next = curr
                right = right.next
            elif curr.val < pivot.val:
                left.next = curr
                left = left.next
            else:
                eq.next = curr
                eq = eq.next
            curr = curr.next

        return quicksort_ll(left.next) + eq.next + quicksort_ll(right.next)

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(4)
    ll.append(3)
    ll.append(2)
    ll.append(1)

