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











################################################################################
#O(n) worst case scenario you would have to visit each node

# class Solution(object):
#     def return_height(self, root):
#         print "inside the correct function"
        
#         if root is None:
#             return 0
        
#         left = self.return_height(root.left)
#         right = self.return_height(root.right)
        
#         if left == -1 or right == -1:
#             print "inside -1"
#             return -1
#         if abs(left-right) >1:
#             print 'inside -1'
#             return -1
        
#         return max(left, right) + 1
    
#     def isBalanced(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if root is None:
#             return True
       
#         if self.return_height(root) == -1:
#             return False
#         return True



# if __name__ == '__main__':
#     # Create sample tree and search for nodes in it
#     five_three = BinarySearchNode(1)
#     one_two = BinarySearchNode(1)
#     one = BinarySearchNode(1)
#     five_two = BinarySearchNode(5, None, five_three)
#     four = BinarySearchNode(4, one, one_two)
#     five = BinarySearchNode(5, four, five_two)