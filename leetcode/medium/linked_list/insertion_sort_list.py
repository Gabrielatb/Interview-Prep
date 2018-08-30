# Sort a linked list using insertion sort.



class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

        self.tail = new_node

    def insertion(self):
        if self.head is None:
            return None

            




if __name__ == '__main__':
    ll = LinkedList()
    ll.append(5)
    ll.append(7)
    ll.append(2)
    ll.append(3)
    ll.append(13)





#insertion sort with list
# def insertion(lst):

#     for i in range(len(lst)):
#         while i > 0:
#             if lst[i] < lst[i-1]:
#                 temp = lst[i]
#                 lst[i] = lst[i-1]
#                 lst[i-1] = temp
#             i -=1
#     return lst


# print(insertion([5,4,3,2,1]))