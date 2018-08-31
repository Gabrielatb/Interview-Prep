#4.3
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

            cur.next = new_node
        self.tail = new_node


class BT(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def create_ll(root):

    level = [root]


    while level:
        new_level = []
        ll = LinkedList()
        prev = None
        for data in level:
            node = ll.append(data)
            node.next = prev
            prev = node

        for data in level:
            if node.left:
                new_level.append(node.left.val)
            if node.right:
                new_level.append(node.right.val)
        level = new_level







#  BST 

#    3
# 9     20
     
#      15   7

# return: 3
#         9 -> 20
#         15 -> 7