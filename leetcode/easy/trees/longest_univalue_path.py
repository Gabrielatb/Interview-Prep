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


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




#Time Complexity O(n), n is number of nodes in a tree
#Space Complexity(O(h)) which is height of tree, recursive call stack will be H layers deep
class Solution(object):
    def depth_first_search(self, root):
            if root is None:
                return 0
            left = self.depth_first_search(root.left)
            right = self.depth_first_search(root.right)
        
            if root.left and root.left.val == root.val:
                left +=1
            else:
                left =0
            if root.right and root.right.val == root.val:
                right +=1
            else:
                right =0     
                
            self.count = max(self.count, left+right)
            return max(left, right)
     
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.depth_first_search(root)
        return self.count














# if __name__ == '__main__':
#     # Create sample tree and search for nodes in it
#     five_three = BinarySearchNode(1)
#     one_two = BinarySearchNode(1)
#     one = BinarySearchNode(1)
#     five_two = BinarySearchNode(5, None, five_three)
#     four = BinarySearchNode(4, one, one_two)
#     five = BinarySearchNode(5, four, five_two)