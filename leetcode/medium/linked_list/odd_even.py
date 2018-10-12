# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Example 1:

# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# Example 2:

# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL



class Node(object):
    def __init__(self, data):
        self.val = data
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

    def print_list(self):
        curr = self.head

        while curr:
            print curr.val
            curr = curr.next
# Time O(n)
# Space O(1)
    def odd_even(self):

        if self.head is None:
            return None

        odd = self.head
        even_head = self.head.next
        even = self.head.next
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        print self.print_list()
        return self.head

       
        # while odd_head.next:
        #     print 'inside of second for loop'
        #     print odd_head
        #     odd_head = odd_head.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.odd_even()
        

































