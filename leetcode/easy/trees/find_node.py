#find node in a binary tree

class BT(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


    def find_node(self, root, data):

        if root is None:
            return None

        if root.data == data:
            return root.data

        left = self.find_node(root.left)
        right = self.find_node(root.right)

        if left is None and right is None:
            return None
        if left or right:
            return left or right


#Call Stack
#___________
#f(None)
#f(3)
#f(5)        


   #   5
   # /   \
   # 3    7
   #     /
   #     6

if __name__ == '__main__':
    six = BT(6)
    three = BT(3)
    seven = BT(7, six)
    five = BT(5, three, seven)
