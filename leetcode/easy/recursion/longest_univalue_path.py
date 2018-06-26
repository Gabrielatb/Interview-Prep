# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

# Note: The length of path between two nodes is represented by the number of edges between them.

# Example 1:

# Input:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:

# 2
# Example 2:

# Input:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:

# 2
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

class BinarySearchNode(object):
    """Binary tree node."""

    def __init__(self, key, left=None, right=None):
        self.val = key

        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode %s>" % self.data

    def longestUnivaluePath(self, root):
      """
      :type root: TreeNode
      :rtype: int
      """
      if root.left is None and root.right is None:
        return -1 
      if root.left.val == root.val:
        left_subtree = self.longestUnivaluePath(root.left)
      left_subtree = -1
      if root.right.val == root.val:
        right_subtree = self.longestUnivaluePath(root.right)
      right_subtree = -1
      return max(left_subtree, right_subtree) + 1

        



if __name__ == '__main__':
    # Create sample tree and search for nodes in it
    five_three = BinarySearchNode(1)
    one_two = BinarySearchNode(1)
    one = BinarySearchNode(1)
    five_two = BinarySearchNode(5, None, five_three)
    four = BinarySearchNode(4, one, one_two)
    five = BinarySearchNode(5, four, five_two)