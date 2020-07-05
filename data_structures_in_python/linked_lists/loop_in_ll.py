# Problem Statement #
# By definition, a loop is formed when a node in your linked list points to a previously traversed node.

# You must implement the detect_loop() function which will take a linked list as input and deduce whether or not a loop is present.

# Input #
# A singly linked list.

# Output #
# Returns True if the given linked list contains a loop. Otherwise, it returns False

# Sample Input #
# LinkedList = 7->14->21->7 # Both '7's are the same node. Not duplicates.
# Sample Output #
# True

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

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

    #  O(n)
    def detect_loop(self):
        if self.head.data == None:
            return False

        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False





zero = Node(0)
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
ll = LinkedList()
ll.insert_at_head(zero)
ll.insert_at_head(one)
ll.insert_at_head(two)
ll.insert_at_head(three)
ll.insert_at_head(four)
# ll.insert_at_head(zero)
print(ll.detect_loop())
# ll.print_lst()






