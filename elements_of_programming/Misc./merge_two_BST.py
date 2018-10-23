#merge two BST to be height balanced
class Node(object):
    def __init__(self, data):
        self.val = data

class BT(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def print_bt(root):
    if root is None:
        return 
    print root.val

    print_bt(root.left)
    print_bt(root.right)





if __name__ == '__main__':
    two = BT(2)
    eleven = BT(11)
    five = BT(5, two, eleven)
    twentythree = BT(23)
    seventeen  = BT(17, five, twentythree)


    three = BT(3) 
    seven = BT(7, three) 
    nineteen = BT(19)
    thirteen = BT(13, seven, nineteen)
