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
    def find_mid(self, head):
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, l, r):
        dummy = dummy_head = Node(0)

        while l and r:
            if l.val < r.val:
                dummy.next = l
                l = l.next
            else:
                dummy.next = r
                r = r.next
            dummy = dummy.next

        if l:
            dummy.next = l
        if r:
            dummy.next = r

        return dummy_head.next

    def merge_sort(self, head):

        if head is None or head.next is None:
            return head

        mid = self.find_mid(head)
        right = mid.next
        mid.next = None
        left = head
        
        l = self.merge_sort(left)
        r = self.merge_sort(right)
        return self.merge(l, r)








if __name__ == '__main__':
    ll = LinkedList()
    ll.append(4)
    ll.append(3)
    ll.append(2)
    ll.append(1)

    new_head = ll.merge_sort(ll.head)
    ll1 = LinkedList()
    ll1.head = new_head
    print ll1.print_list()
