class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def print_list(self):
        if self.head == None:
            print("NO list")
        else:
            curr = self.head
            while curr.next:
                print(curr.data, end = " -> ")
                curr = curr.next
            print(curr.data, end = " -> None ")

    # O(n)
    def search(self, value):
        if self.head == None:
            print("Value not present in list")
            return False
        else:
            curr = self.head
            while curr:
                if curr.data == value:
                    return True
                curr = curr.next
            return False
                




ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
print(ll.search(30))
