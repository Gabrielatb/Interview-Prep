#implement a function to check if a bt is balanced

class BinarySearchNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def height(self, root):

        
        if root is None:
            return -1

        if root.left is None and root.right is None:
            return 0

        if root.left is None:
            right = self.height(root.right) + 1

        if root.right is None:
            left = self.check_balanced(root.left) + 1

        return max(self.check_balanced(root.left) - self.check_balanced(root.right)) + 1


    def is_balanced(self, root):
        if root is None:
            return None

        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False

        return True








if __name__ == '__main__':

    two = BinarySearchNode('two')
    seventeen = BinarySearchNode('seventeen', None, two)
    fifteen = BinarySearchNode('fifteen')
    twenty = BinarySearchNode('twenty', fifteen, seventeen)
    nine = BinarySearchNode('nine')
    three = BinarySearchNode('three', nine, twenty)