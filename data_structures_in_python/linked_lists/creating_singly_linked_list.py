class Node:
    def __init__(self, data):
        self.data = data # data of the node
        self.next = None # pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None
    #O(1)
    def get_head(self):
        return self.head
    # O(1)
    def is_empty(self):
        if self.head == None:
            return True
        return False
    # O(1)
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return self.head
    # O(n)
    def print_lst(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        node = self.head
        while node.next:
            print(node.data, end=" -> ")
            node = node.next
        print(node.data, "-> None")
        return True
    # O(n)
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        curr = self.head 
        while curr.next:
            print(curr.data, end=" -> ")
            curr = curr.next
        curr.next = new_node
        print(new_node.data, "-> None")

    def insert_at_k(self, data, k):
        # new_node = Node(data)
        # if self.is_empty():
        #     self.head = new_node
        #     return
        # curr = self.head 
        # while curr.next:
        #     print(curr.data, end=" -> ")
        #     curr = curr.next
        # curr.next = new_node
        # print(new_node.data, "-> None")





link_list = LinkedList()
# print(link_list.get_head())
# print(link_list.is_empty())

print("Inserting values in list")
for i in range(1, 10):
    link_list.insert_at_head(i)
# link_list.print_lst()
link_list.insert_at_tail(200)