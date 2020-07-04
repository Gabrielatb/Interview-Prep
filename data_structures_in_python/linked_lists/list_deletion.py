class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def is_empty(self):
        if self.head:
            return False
        return True

    def print_lst(self):
        if self.is_empty():
            print ("List is Empty")
            return False

        curr = self.head 

        while curr.next:
            print (curr.data, end="->")
            curr = curr.next
        print(curr.data, end="->None")
        print("")
        return True

    def delete_at_head(self):
        print ("inside delete at head")
        if self.is_empty():
            return False

        curr = self.head
        self.head = self.head.next
        curr.next = None
        return True

    # O(n)
    def delete_at_value(self, value):
        if self.is_empty():
            return False

        if self.head.data == value:
            self.delete_at_head()
            return True

        prev = None
        curr = self.head
        while curr.next:
            if curr.data == value:
                prev.next = curr.next
                curr.next = None
                return True
            prev = curr
            curr = curr.next

        if curr.data == value:
            prev.next = curr.next
            curr.next = None
            return True
        return False




ll = LinkedList()

for num in range(1, 11)[::-1]:
    ll.insert_at_head(num)

ll.print_lst()
ll.delete_at_value(10)
ll.print_lst()
