# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL


class Node(object):
    """Creating Node in a Linked List """

    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        # node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = node

    def print_list(self):
        current = self.head

        while current is not None:
            print current.val
            current = current.next

    def reverse_list(self, head):
        #iterative solution
        prev = None
        current = head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def reverseList(self, head):
        #recursive solution
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        prev = None
        return self.reverse(current)
    
    def reverse(self, current, prev=None):
        
            if current is None:
                return prev

            temp = current.next
            current.next = prev
            return self.reverse(temp, current)
    


if __name__ == '__main__':
    linked_list = LinkedList()
    one = Node(1)
    linked_list.append(one)
    two = Node(2)
    linked_list.append(two)
    three = Node(3)
    linked_list.append(three)
    four = Node(4)      
    linked_list.append(four)