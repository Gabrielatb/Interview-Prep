# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

# Given linked list -- head = [4,5,1,9], which looks like following:

#     4 -> 5 -> 1 -> 9
# Example 1:

# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list
#              should become 4 -> 1 -> 9 after calling your function.
# Example 2:

# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list
#              should become 4 -> 5 -> 9 after calling your function.
# Note:

# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the linked list.
# Do not return anything from your function.


# Iplementation of basic insertion and traversal of a linked list. From mycodeschool, in addition to other functions I have added


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


    def delete(self, node):

        node.val = node.next.val
        node.next = node.next.next



        






if __name__ == '__main__':
    linked_list = LinkedList()
    apple = Node('apple')
    linked_list.append(apple)
    berry = Node('berry')
    linked_list.append(berry)
    cherry = Node('cherry')
    linked_list.append(cherry)
