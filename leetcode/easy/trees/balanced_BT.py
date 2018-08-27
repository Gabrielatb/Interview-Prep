# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#     Example 1:

# Given the following tree [3,9,20,null,null,15,7]:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.

# Example 2:

# Given the following tree [1,2,2,3,3,null,null,4,4]:

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4

#Time Complexity: O(n)
#worse case scenario you traverse all nodes

#Space Complexity: O(h)
#height of tree
class BST(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def height(self, root):
        """
        >>> three.is_balanced(three)
        True

        >>> one.is_balanced(one)
        False

        """

        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)


        if left == -1 or right == -2 or abs(left-right) > 1:
            return -1

        return max(left, right) + 1


    def is_balanced(self, root):

        height = self.height(root)
        # print height

        if height == -1:
            return False

        return True



    # Create sample tree and search for nodes in it
if __name__ == '__main__':
    fifteen = BST(15)
    seven = BST(7)
    nine = BST(9)
    twenty = BST(20, fifteen, seven)
    three = BST(3, nine, twenty)



    four_1 = BST(4)
    four_2 = BST(4)
    three_1 = BST(3, four_1, four_2)
    three_2 = BST(3)
    two_1 = BST(2, three_1, three_2)
    two_2 = BST(2)
    one = BST(1, two_1, two_2)

    import doctest
    if doctest.testmod().failed == 0:
        print "*****Solution Correct!******"


