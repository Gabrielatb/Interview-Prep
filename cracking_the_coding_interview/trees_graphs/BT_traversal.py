class BinarySearchNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def inorder(self):
        #left, root, right

        if self is None:
            return None

        if self.left:
            self.left.inorder()

        print self.data

        if self.right:
            print self.right.inorder()


    def preorder(self):
        #root, left, right

        if self is None:
            return None

        print self.data

        if self.left:
            self.left.preorder()


        if self.right:
            self.right.preorder()


        return
    def postorder(self):
        #left, right, root


        if self is None:
            return None

        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()

        print self.data










if __name__ == '__main__':

    seventeen = BinarySearchNode('seventeen')
    fifteen = BinarySearchNode('fifteen')
    twenty = BinarySearchNode('twenty', fifteen, seventeen)
    nine = BinarySearchNode('nine')
    three = BinarySearchNode('three', nine, twenty)