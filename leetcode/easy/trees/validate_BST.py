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
    # def isValidBST(self):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
        # stack = []
        # if self is None:
        #     return True
        # elif root.left:
        #     left = self.left
        #     left.isValidBST()
        # if root not in stack:
        #     stack.append(root)
        # if root.right:
        #     right = root.right
        #     right.isValidBST()
        # for i in range(len(stack) - 1):
        #     if stack[i] > stack[i+1]:
        #         return False 
        #     return True
 
    def helper(self, root, validate_list):
        if root is None:
            return None
        if root.left:
            left = root.left
            # print "this is left" + str(left)
            left.helper(left, validate_list)
        validate_list.append(root.val)
        # print validate_list   
        if root.right:
            right = root.right
            # print "this is right" + str(right)
            right.helper(right, validate_list)
    def check_BST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        validate_list = []
        root.helper(root, validate_list)
        # print "finishing off in the inorder function"
        print validate_list
        for i in range(len(validate_list)-1):
            print validate_list[i], validate_list[i+1]
            if validate_list[i] >= validate_list[i+1]:
                return False
        return True







if __name__ == '__main__':
    # Create sample tree and search for nodes in it
    # five_three = BinarySearchNode(5)
    # one_two = BinarySearchNode(3)
    # one = BinarySearchNode(1)
    # five_two = BinarySearchNode(5, None, five_three)
    # four = BinarySearchNode(2, one, one_two)
    # five = BinarySearchNode(5, four, five_two)

    three = BinarySearchNode(3)
    one = BinarySearchNode(1)
    two = BinarySearchNode(2, one, three)