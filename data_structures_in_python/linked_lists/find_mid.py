# Problem Statement #
# You have to implement the find_mid() function which will take a linked list as an 
# input and return the value of the middle node. 
# If the length of the list is even, the middle value will occur at \frac{length}{2}
# ​2
# ​
# ​length
# ​​ . For a list of odd length, the middle value will be \frac{length}{2}+1
# ​2
# ​
# ​length
# ​​ +1.

# Input #
# A singly linked list.

# Output #
# The integer value of the middle node.

# Sample Input #
# LinkedList = 7->14->10->21
# Sample Output #
# 14

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

    def find_legnth(self):
        curr = self.head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length

    #  O(n)
    def find_mid(self):
        if self.head == None:
            return -1
        mid = self.find_legnth() // 2
        if (self.find_legnth() % 2):
            mid += 1 

        curr = self.head
        for i in range(mid -1):
            curr = curr.next
        return curr.data

    # O(n)
    def find_mid(self):
        if self.head == None:
            return -1

        if self.head.next == None:
            # Only one element exists in the list
            return self.head.data

        slow = self.head
        fast = self.head.next.next
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        if slow:
            return slow.data
        return -1




ll = LinkedList()
for num in range(1, 11)[::-1]:
    ll.insert_at_head(num)

ll.print_lst()
ll.find_mid()
# ll.insert_at_head(zero)
# print(ll.detect_loop())
# ll.print_lst()


