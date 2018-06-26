# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted array: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

class BinarySearchNode(object):
    """Binary tree node."""

    def __init__(self, key, left=None, right=None):
        self.val = key

        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode %s>" % self.val

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        mid = len(nums)/2
        node = BinarySearchNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return node









if __name__ == '__main__':
#     five_three = BinarySearchNode(5)
#     one_two = BinarySearchNode(3)
#     one = BinarySearchNode(1)
#     five_two = BinarySearchNode(5, None, five_three)
#     four = BinarySearchNode(2, one, one_two)
#     five = BinarySearchNode(5, four, five_two)

     # three = BinarySearchNode(3)
     # one = BinarySearchNode(1)
    # two = BinarySearchNode(2, one, three)