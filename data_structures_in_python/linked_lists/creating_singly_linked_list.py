class Node:
    def __init__(self, data):
        self.data = data # data of the node
        self.next = None # pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None
    # O(1)
    def get_head(self):
        return self.head
    # O(1)
    def is_empty(self):
        if self.head:
            return False
        return True
    # O(1)
    def insert_at_head(self, data):
        print("inserting at head", data)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    # O(n)
    def print_lst(self):
        if (self.is_empty()):
            print("List is Empty!")
            return False
        curr = self.head
        while curr.next:
            print(curr.data, end="=>")
            curr = curr.next
        print(curr.data, end="=>None")
        print("")
        return True
    # O(n)
    def insert_at_tail(self, data):
        new_node = Node(data)
        if (self.is_empty()):
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node



link_list = LinkedList()
print(link_list.get_head())
print(link_list.is_empty())

print("Inserting values in list")
for i in range(1, 11):
    link_list.insert_at_head(i)
link_list.print_lst()
link_list.insert_at_tail(200)
link_list.print_lst()
