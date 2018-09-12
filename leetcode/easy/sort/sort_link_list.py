# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5


class Node(object):
    def __init__(self, data):
        self.val = data
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

    def print_list(self):
        if self.head is None:
            return "No list to print"
        else:
            curr = self.head
            while curr:
                print curr.val
                curr = curr.next

def find_mid(head):
    slow= head
    fast = head
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow
        #Right
#left = 4 --> 2 -->None right = 1 --> 3 --> None
def merge_sort(head):

    if head is None or head.next is None:
        return head

    mid = find_mid(head)
    right = mid.next
    mid.next = None
    left = head
    return merge(merge_sort(left), merge_sort(right))
  

def merge(left, right):
    dummy = dummy_head = Node(0)
    while left and right:
        if left.val > right.val:
            dummy.next = right
            right = right.next
        else:
            dummy.next = left
            left = left.next   
        dummy = dummy.next
    if left:
        dummy.next = left
    if right:
        dummy.next = right

    return dummy_head.next             

    

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(4)
    ll.append(2)
    ll.append(1)
    ll.append(3)

    
    new_head = merge_sort(ll.head)
    ll1 = LinkedList()
    ll1.head = new_head
    ll1.print_list()
