class Node(object):
    """Creating Node in a Linked List """

    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = node
        self.tail = node


    def print_list(self):
        current = self.head

        while current is not None:
            print current.val
            current = current.next

    def reverse(self):
        
        curr = self.head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def isPalindrome(self):
        """
        :type head: ListNode
        :rtype: bool
        """
        # self.print_list(self.head)
    
        reversed_ll = self.reverse(self.head)
        self.print_list(reversed_ll)
        
        # while curr and reversed_ll:
        #     print curr.val, reversed_ll.val
            
        #     if curr.val != reversed_ll.val:
        #         return False
        #     else:
        #         reversed_ll = reversed_ll.next
        #         curr = curr.next
        # return True


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    # print ll.isPalindrome()
    ll.print_list
  



