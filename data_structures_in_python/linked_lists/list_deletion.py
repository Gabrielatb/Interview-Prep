class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node


    def print_list(self):
        if self.head == None:
            print("Empty List!")
        else:
            curr = self.head
            while curr.next:
                print(curr.data, end="->")
                curr = curr.next
            print(curr.data, end="->None")

    # O(1)
    def delete_at_head(self):
        if self.head == None:
            print("Empty List!")
        else:
            head_to_delete = self.head
            self.head  = self.head.next
            head_to_delete.next = None

    # O(N)
    # def delete_at_value(self, value):
    #     if self.head == None:
    #         print("Empty List!")
    #         return False
    #     else:
    #         curr = self.head
    #         prev = None
    #         while curr:
    #             if curr.data == value:
    #                 curr.next = prev
    #                 return True
    #             prev = curr
    #             curr = curr.next
    #         return False


# 1 -> 2 -> 3 -> 4 -> 5 -> None

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
# ll.delete_at_head()
print(ll.delete_at_value(4))
ll.print_list()
