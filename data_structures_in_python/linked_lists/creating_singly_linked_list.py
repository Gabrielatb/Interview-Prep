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

link_list = LinkedList()
print(link_list.get_head())
print(link_list.is_empty())
