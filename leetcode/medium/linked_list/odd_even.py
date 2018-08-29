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

    def print_list(self):
        curr = self.head

        while curr:
            print curr.data
            curr = curr.next

    def odd_even(self):
        #Time Complexity O(n)
        #Space Complexity O(1)

        count = 1
        even = even_head = Node(0)
        odd = odd_head = Node(0)

        curr = self.head

        while curr:
            if count % 2 != 0:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next

            curr = curr.next
            count +=1
        even.next = None

        odd.next = even_head.next

        result = odd_head.next
    
        while result:
            print result.data
            result = result.next
        return 'done'







if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

