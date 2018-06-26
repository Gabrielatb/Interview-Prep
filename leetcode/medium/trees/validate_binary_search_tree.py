# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:

# Input:
#     2
#    / \
#   1   3
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
#              is 5 but its right child's value is 4.

class BinarySearchNode(object):
    """Binary tree node."""

    def __init__(self, key, left=None, right=None):
        self.val = key

        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode %s>" % self.val

    def validate_BST(self):

        # queue = [self]


        # while queue:
        #     node = queue.pop(0)
        #     print queue
        #     print node
        #     if node.right is not None and node.left is not None:
        #         if node.right.val <= node.left.val:
        #             return False
        #         if node.right.val <= node.val:
        #             return False
        #         if node.left.val < node.val and node.right.val > node.val:
        #             queue.append(node.left)
        #             queue.append(node.right)
                    
        #     elif node.right is not None:
        #         if node.right.val <= node.val:
        #             return False
        #         if node.right.val <= root.val:
        #             return False
        #         if node.right.val > node.val:
        #             queue.append(node.right)
        #     elif node.left is not None:
        #         if node.left.val >= node.val:
        #             return False
        #         if node.left.val <= root.val:
        #             return False
        #         if node.left.val < node.val:
        #              queue.append(node.left)
        # return True

        if self is None:
            return True
        if self.left is not None and self.right is not None:
            
        if self.left:
            # left = self.left
             self.left = self.left.validate_BST()
             if self.left.val >= self.val:
                return False
        if self.right:
            # right = self.right
            self.right = self.right.validate_BST()
            if self.right.val >= self.right.val:
                return False


if __name__ == '__main__':
    # seventeen = BinarySearchNode(17)
    # fifteen = BinarySearchNode(15)
    # twenty = BinarySearchNode(20, fifteen, seventeen)
    # nine = BinarySearchNode(9)
    # three = BinarySearchNode(3, nine, twenty)

    # one_two = BinarySearchNode(1)
    # one = BinarySearchNode(1, None, one_two)



    twenty = BinarySearchNode(20)
    six = BinarySearchNode(6)
    fifteen= BinarySearchNode(15, six, twenty)
    five = BinarySearchNode(5)
    ten = BinarySearchNode(10, five, fifteen)





