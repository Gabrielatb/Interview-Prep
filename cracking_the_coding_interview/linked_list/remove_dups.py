#write code to remove duplicates from an unsorted linked list

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next=None

class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

        self.tail = new_node


if __name__ == '__main__':
    ll = LinkedList()
    one = ll.append(1)
    one_1=ll.append(1)
    two = ll.append(2)
    two_2 = ll.append(2)
    two_3 = ll.append(2)
    three = ll.append(3)
    four =ll.append(4)
    five = ll.append(5)
    five_2 = ll.append(5)
    five_3 = ll.append(5)
    five_4 = ll.append(5)





























#################################################################################
# class ListNode(object):
#     def __init__(self, data):
#         self.val = data
#         self.next = None

# class LinkedList(object):
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self, data):

#         new_node = ListNode(data)

#         if self.head is None:
#             self.head = new_node

#         elif self.tail is not None:
#             self.tail.next = new_node

#         self.tail = new_node

#     def print_list(self):

#         curr = self.head

#         while curr:
#             print curr.val
#             curr = curr.next

#     def remove_dups(self):

#         curr = self.head

#         while curr.next:
#             if curr.next.val == curr.val:
#                 curr.next = curr.next.next
#             else:
#                 curr = curr.next

#         return self.print_list()











# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(1)
#     ll.append(1)
#     ll.append(2)
#     ll.append(3)
#     ll.append(3)
#     ll.append(3)
#     ll.append(4)
#     ll.append(4)
