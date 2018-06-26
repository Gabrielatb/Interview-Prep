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

    def insert(self, data, n):

        new_node = Node(data)
        count = 0
        if self.head is None:
            self.head = new_node
        current = self.head
        prev_node = None
        while current is not None:
            count += 1
            if count == n:
                prev_node.next = new_node
                new_node.next = current

            else:
                prev_node = current
                current= current.next




  

        






if __name__ == '__main__':
    linked_list = LinkedList()
    apple = Node('apple')
    linked_list.append(apple)
    berry = Node('berry')
    linked_list.append(berry)
    cherry = Node('cherry')
    linked_list.append(cherry)