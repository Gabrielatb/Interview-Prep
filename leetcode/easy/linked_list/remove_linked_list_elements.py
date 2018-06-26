# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

class Node(object):
    """Creating Node in a Linked List """

    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        # node = Node(data)

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


    def remove_elements(self, head, val):
       if head is None:
            return None
        current = head
        prev = None
        while current is not None:
            if current.val == val:
                if prev:
                    prev.next = current.next
                else:
                    head = current.next
            else:
                prev = current
            current = current.next
        return head
        

if __name__ == '__main__':
    linked_list = LinkedList()
    apple = Node('apple')
    linked_list.append(apple)
    berry = Node('berry')
    linked_list.append(berry)
    cherry = Node('cherry')
    linked_list.append(cherry)
    berry = Node('berry')      
    linked_list.append(berry)
