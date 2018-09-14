# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

class Node(object):
    """Creating Node in a Linked List """

    def __init__(self, data):
        self.val = data
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

            while current.next:
                current = current.next
            current.next = node
        self.tail = node


    def print_list(self):
        current = self.head

        while current is not None:
            print current.val
            current = current.next

 # 4->2->1->3
def find_mid(head):
    fast = head
    slow = head

    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow
def merge(l,r):
    dummy = dummy_head = Node(0)
    while l and r:
        if l.val > r.val:
            dummy.next = r
            r = r.next
        else:
            dummy.next = l
            l = l.next
        dummy = dummy.next

    if l:
        dummy.next = l 

    if r:
        dummy.next = r

    return dummy_head.next

def merge_list(head):

    if head is None or head.next is None:
        return head
    mid = find_mid(head)
    right = mid.next
    mid.next = None
    left = head

    l = merge_list(left)
    r = merge_list(right)
    return merge(l,r)

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(4)
    ll.append(2)
    ll.append(1)
    ll.append(3)
    # print merge_list(ll.head)

