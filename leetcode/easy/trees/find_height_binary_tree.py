            #  5
            #  /\
            # 4  6
            # /    \
            # 3     7







class BT(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def find_height(self):

        


        



if __name__ == '__main__':
    three = BT(3)
    seven = BT(7)
    six = BT(6, None, seven)
    four = BT(4, three)
    five = BT(5, four, six)





















#find height of binary search tree
# class BinarySearchNode(object):
#     """Binary tree node."""

#     def __init__(self, key, left=None, right=None):
#         self.data = key

#         self.left = left
#         self.right = right

#     def __repr__(self):
#         """Debugging-friendly representation."""

#         return "<BinaryNode %s>" % self.data

#     def find_height(self, root):
#         #height of empty tree is -1
#         if root is None:
#             return -1
#         left_height = self.find_height(root.left)
#         print left_height
#         right_height = self.find_height(root.right)
#         print right_height

#         return max(left_height, right_height) + 1 


        
# if __name__ == '__main__':
# # Create sample tree and search for nodes in it
#     five_three = BinarySearchNode(1)
#     one_two = BinarySearchNode(1)
#     one = BinarySearchNode(1)
#     five_two = BinarySearchNode(5, None, five_three)
#     four = BinarySearchNode(4, one, one_two)
#     five = BinarySearchNode(5, four, five_two)