
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Traversing above BST depth-first search: preorder, inorder, postorder

class BinarySearchNode(object):
    """Binary tree node."""

    def __init__(self, key, left=None, right=None):
        self.data = key

        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode %s>" % self.data

    def preorder(self):
        """
        :type root: TreeNode
        :rtype: int
        """
        #iterative
        if self is None:
            return 
        print self.data
        if self.left:
            left = self.left
            left.preorder()
        if self.right:
            right = self.right
            right.preorder()

        


    def inorder(self):
        """
        :type root: TreeNode
        :rtype: int
        """
        if self is None:
            return 
        if self.left:
            left = self.left
            left.inorder()
        print self.data     
        if self.right:
            right = self.right
            right.inorder()

    def postorder(self):
        """
        :type root: TreeNode
        :rtype: int
        """
        if self is None:
            return 
        if self.left:
            left = self.left
            left.postorder()  
        if self.right:
            right = self.right
            right.postorder()
        print self.data   


if __name__ == '__main__':
    # Create sample tree and search for nodes in it
    seventeen = BinarySearchNode('seventeen')
    fifteen = BinarySearchNode('fifteen')
    twenty = BinarySearchNode('twenty', fifteen, seventeen)
    nine = BinarySearchNode('nine')
    three = BinarySearchNode('three', nine, twenty)