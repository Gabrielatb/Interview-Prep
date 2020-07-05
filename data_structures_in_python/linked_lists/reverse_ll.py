# Problem Statement #
# You have written the reverse function, which takes a singly linked list and produces the exactly opposite list.

# Input #
# A singly linked list.

# Output #
# The reversed linked list.

# Sample Input #
# LinkedList = 0->1->2->3-4
# Sample Output #
# LinkedList = 4->3->2->1->0

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

    def print_lst(self):
        if self.head == None:
            print("Empty List!")
            return False

        curr = self.head
        while curr.next:
            print (curr.data, end="->")
            curr = curr.next
        print(curr.data, end='->None')
        print('')
        return True

    # O(n)
    def reverse(self):
        if self.head == None:
            print("Empty List!")
            return self.head


        curr = self.head
        next = None
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

            self.head = prev
        return self.head
            






ll = LinkedList()
for num in range(1,11)[::-1]:
    ll.insert_at_head(num)
ll.print_lst()
ll.reverse()
ll.print_lst()







