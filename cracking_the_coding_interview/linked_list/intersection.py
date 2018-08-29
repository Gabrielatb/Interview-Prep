#problem number 2.7


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
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
        return new_node

    def append1(self, data):
        new_node = data
        if self.head is None:
            self.head = new_node

        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

        self.tail = new_node


    def print_list(self):
        if self.head is None:
            print "no nodes to print"


        curr = self.head
        while curr:
            print curr
            curr = curr.next


def intersection(ll1, ll2):


    #a1 -> a2  
    #            ->c1 -> c2 ->c3
    #b1 -> b2 ->b3


    length1 = 0
    length2 = 0

    curr1 = ll1.head
    curr2 = ll2.head

    while headA:
        headA = headA.next
        length1 +=1


    while headB:
        headB = headB.next
        length1 +=1

    while length1 > length2:
        curr1 = curr1.next
        length1 -=1

    while length2 > length1:
        curr2 = curr2.next
        length2 -=1


    while curr1 and curr2:
        if curr1 == curr2:
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next


# time complexity: O(m+n)
# space complexity O(1)
























#         